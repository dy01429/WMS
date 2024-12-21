import cv2
import numpy as np
import torch
from datetime import datetime
import logging
import mysql.connector

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')

# Load YOLO model
logging.info("Loading custom YOLO model...")
custom_model_path = r"C:\Users\ethan\Downloads\Demo8\yolov5\runs\train\custom_pallet_box_model\weights\best.pt"
model = torch.hub.load('ultralytics/yolov5', 'custom', path=custom_model_path, force_reload=True)
model.conf = 0.25
model.iou = 0.6
logging.info("Custom YOLOv5 model loaded successfully.")

# Initialize tracking
pallet_tracks = {}
pallet_distances = {}
pallet_positions = {}
pallet_zones = {}
next_pallet_id = 0
size_threshold = 100
stabilization_threshold = 5
proximity_threshold = 50

# Database connection with error handling
try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Rasscal14',
        database='warehouse'
    )
    cursor = conn.cursor()
    logging.info("Database connection established successfully.")
except mysql.connector.Error as err:
    logging.error(f"Error connecting to the database: {err}")
    exit(1)

# Function to calculate Euclidean distance
def calculate_distance(start, end):
    x1, y1 = start
    x2, y2 = end
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Determine the zone for a given point
def get_zone(centroid, width, height):
    x, y = centroid
    if x < width // 2 and y < height // 2:
        return "Zone A"
    elif x >= width // 2 and y < height // 2:
        return "Zone B"
    elif x < width // 2 and y >= height // 2:
        return "Zone C"
    else:
        return "Zone D"

# Draw zones on the video feed
def draw_zones(frame):
    height, width = frame.shape[:2]
    cv2.line(frame, (width // 2, 0), (width // 2, height), (255, 0, 0), 2)
    cv2.line(frame, (0, height // 2), (width, height // 2), (255, 0, 0), 2)

    zones = {
        "Zone A": (10, 30),
        "Zone B": (width // 2 + 10, 30),
        "Zone C": (10, height // 2 + 30),
        "Zone D": (width // 2 + 10, height // 2 + 30),
    }

    for label, (x, y) in zones.items():
        cv2.putText(frame, label, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

# Group boxes into pallets based on proximity
def group_boxes_into_pallets(boxes, threshold=proximity_threshold):
    grouped_pallets = []
    while boxes:
        box = boxes.pop(0)
        pallet = [box]
        for other_box in boxes[:]:
            centroid1 = ((box[0] + box[2]) // 2, (box[1] + box[3]) // 2)
            centroid2 = ((other_box[0] + other_box[2]) // 2, (other_box[1] + other_box[3]) // 2)
            if calculate_distance(centroid1, centroid2) < threshold:
                pallet.append(other_box)
                boxes.remove(other_box)
        grouped_pallets.append(pallet)
    return grouped_pallets

# Process video and track pallets
def process_video_and_track(video_path, skip_interval=10):
    global next_pallet_id
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        logging.error(f"Video file {video_path} could not be opened.")
        return

    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Skip frames for faster processing
        if frame_count % skip_interval != 0:
            frame_count += 1
            continue

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = model(frame_rgb)
        detections = results.pandas().xyxy[0]

        # Extract detected boxes
        boxes = []
        for _, detection in detections.iterrows():
            x1, y1, x2, y2, conf, cls = detection[['xmin', 'ymin', 'xmax', 'ymax', 'confidence', 'class']]
            label = model.names[int(cls)].lower()

            if label == "box" and conf >= model.conf:
                width = int(x2 - x1)
                height = int(y2 - y1)
                if width >= size_threshold and height >= size_threshold:
                    boxes.append((int(x1), int(y1), int(x2), int(y2)))

        grouped_pallets = group_boxes_into_pallets(boxes)

        for pallet_boxes in grouped_pallets:
            x1 = min(box[0] for box in pallet_boxes)
            y1 = min(box[1] for box in pallet_boxes)
            x2 = max(box[2] for box in pallet_boxes)
            y2 = max(box[3] for box in pallet_boxes)
            centroid = ((x1 + x2) // 2, (y1 + y2) // 2)

            pallet_id = None
            for existing_id, track_data in pallet_tracks.items():
                if calculate_distance(track_data['centroid'], centroid) < proximity_threshold:
                    pallet_id = existing_id
                    break

            if pallet_id is None:
                pallet_id = next_pallet_id  # Use numeric ID
                next_pallet_id += 1
                pallet_distances[pallet_id] = 0
                pallet_positions[pallet_id] = centroid
                pallet_zones[pallet_id] = get_zone(centroid, frame.shape[1], frame.shape[0])

            prev_position = pallet_positions[pallet_id]
            distance = calculate_distance(prev_position, centroid)
            if distance > stabilization_threshold:
                pallet_distances[pallet_id] += distance
                pallet_positions[pallet_id] = centroid
                pallet_zones[pallet_id] = get_zone(centroid, frame.shape[1], frame.shape[0])

            pallet_tracks[pallet_id] = {'centroid': centroid, 'bbox': (x1, y1, x2, y2)}

            color = (0, 255, 0)
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, f"Pallet {pallet_id}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        draw_zones(frame)

        cv2.imshow("Pallet Tracking", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            logging.info("Exiting video playback.")
            break

        frame_count += 1

    cap.release()
    cv2.destroyAllWindows()

    # Store detected pallets
    print("\nDetected Pallets:")
    for pallet_id, distance in pallet_distances.items():
        print(f"Pallet {pallet_id}: Traveled {distance:.2f} units, Last detected in {pallet_zones[pallet_id]}")

    selected_pallets = input("Enter the pallets to store in the database (comma-separated): ").split(",")

    for pallet_id in selected_pallets:
     pallet_id = int(pallet_id.strip())
    if pallet_id in pallet_distances:
        try:
            # Fetch the zone ID for the pallet's current zone
            zone_name = pallet_zones[pallet_id]
            cursor.execute("SELECT zone_id FROM zones WHERE zone_name = %s", (zone_name,))
            zone_id = cursor.fetchone()
            
            if zone_id:
                # Step 1: Insert the pallet into the pallets table
                cursor.execute("""
                    INSERT INTO pallets (pallet_id, pallet_label, total_distance, last_zone_id)
                    VALUES (%s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE
                    total_distance = COALESCE(total_distance, 0) + VALUES(total_distance),
                    last_zone_id = VALUES(last_zone_id)
                """, (pallet_id, f"Pallet {pallet_id}", pallet_distances[pallet_id], zone_id[0]))

                conn.commit()  # Commit the pallets table insert
                logging.debug(f"Pallet {pallet_id} successfully inserted/updated in pallets table.")

                # Step 2: Verify the pallet exists in the pallets table
                cursor.execute("SELECT COUNT(*) FROM pallets WHERE pallet_id = %s", (pallet_id,))
                exists = cursor.fetchone()[0]
                if exists == 0:
                    raise ValueError(f"Pallet {pallet_id} was not found in pallets table after insertion!")

                # Step 3: Insert into the pallet_movements table
                cursor.execute("""
                    INSERT INTO pallet_movements (pallet_id, from_zone_id, to_zone_id)
                    VALUES (%s, %s, %s)
                """, (pallet_id, None, zone_id[0]))

                conn.commit()  # Commit the pallet_movements table insert
                logging.debug(f"Pallet movement for {pallet_id} successfully recorded in pallet_movements table.")

        except mysql.connector.Error as err:
            logging.error(f"Error while storing pallet {pallet_id}: {err}")
            conn.rollback()  # Rollback transaction on error


# Main execution
if __name__ == "__main__":
    video_path = r"C:\Users\ethan\OneDrive\Desktop\vlc-record-2024-09-06-17h39m56s-rtsp___141.165.40.34_stream1-.mp4"
    try:
        process_video_and_track(video_path, skip_interval=20)
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    finally:
        if conn.is_connected():
            conn.close()
            logging.info("Database connection closed.")
