import cv2
import torch
import mysql.connector
from datetime import datetime
import logging
import numpy as np

# Configure logging to both console and a file
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', handlers=[
    logging.FileHandler("stacking_issues.log"),
    logging.StreamHandler()
])

# Load YOLOv5 model
custom_model_path = r"C:\Users\ethan\Downloads\Demo8\yolov5\runs\train\custom_pallet_box_model\weights\best.pt"
model = torch.hub.load('ultralytics/yolov5', 'custom', path=custom_model_path, force_reload=True)
logging.info("Custom YOLOv5 model loaded successfully")

# Set confidence and IoU thresholds
model.conf = 0.3
model.iou = 0.3

# Database connection function
def db_connect():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Rasscal14',
            database='warehouse'
        )
        cursor = conn.cursor()
        return conn, cursor
    except mysql.connector.Error as err:
        logging.error(f"Database connection error: {err}")
        return None, None

conn, cursor = db_connect()

def detect_stacking_issues(boxes):
    """Detect stacking irregularities with dynamic thresholds based on box dimensions."""
    issues = []
    offset_threshold_ratio = 0.1
    overlap_threshold = 0.5
    tilt_threshold_ratio = 0.1

    for i in range(len(boxes) - 1):
        box1, box2 = boxes[i], boxes[i + 1]
        box1_center_x = (box1[0] + box1[2]) / 2
        box2_center_x = (box2[0] + box2[2]) / 2
        box1_width = abs(box1[2] - box1[0])

        offset = abs(box1_center_x - box2_center_x)
        if offset > box1_width * offset_threshold_ratio:
            issues.append(f"Horizontal misalignment detected between Box {i} and Box {i + 1} (offset: {offset}px)")

        vertical_overlap = max(0, min(box1[3], box2[3]) - max(box1[1], box2[1]))
        overlap_ratio = vertical_overlap / (box1[3] - box1[1])
        if overlap_ratio < overlap_threshold:
            issues.append(f"Insufficient vertical overlap between Box {i} and Box {i + 1} (overlap ratio: {overlap_ratio:.2f})")

        if abs(box1_width - abs(box2[2] - box2[0])) > box1_width * tilt_threshold_ratio:
            issues.append(f"Potential tilting or rotation detected between Box {i} and Box {i + 1}")

    layer_y_coordinates = {}
    for j, box in enumerate(boxes):
        layer_key = round(box[3] / 50)
        layer_y_coordinates.setdefault(layer_key, []).append(j)

    for layer, box_indices in layer_y_coordinates.items():
        if len(box_indices) > 1:
            y_positions = [boxes[idx][1] for idx in box_indices]
            if max(y_positions) - min(y_positions) > 10:
                issues.append(f"Uneven stacking in layer {layer} (y-coordinate difference: {max(y_positions) - min(y_positions)}px)")

    return issues

def log_issue(pallet_id, issue_description):
    """Logs stacking issue details into database and console log."""
    logging.info(f"Pallet ID {pallet_id} Issue: {issue_description}")
    if cursor and conn:
        try:
            cursor.execute("INSERT INTO stacking_issues (pallet_id, description, timestamp) VALUES (%s, %s, %s)",
                           (pallet_id, issue_description, datetime.now()))
            conn.commit()
        except mysql.connector.Error as err:
            logging.error(f"Database error: {err}")

def store_stacking_result(pallet_id, issues):
    """Store stacking result in the pallets table by updating pallet_quality."""
    pallet_quality = "Issues Detected" if issues else "Good"
    if cursor and conn:
        try:
            cursor.execute("""
                UPDATE pallets
                SET pallet_quality = %s
                WHERE pallet_id = %s
            """, (pallet_quality, pallet_id))
            conn.commit()
            logging.info(f"Pallet quality '{pallet_quality}' stored for pallet ID {pallet_id}.")
        except mysql.connector.Error as err:
            logging.error(f"Error updating pallet quality for pallet ID {pallet_id}: {err}")

def generate_stacking_report(pallet_id, issues):
    """Generate a textual report of stacking quality for operational use."""
    if issues:
        print(f"Stacking Report for Pallet ID {pallet_id}:")
        for issue in issues:
            print(f" - {issue}")
    else:
        print(f"Stacking Report for Pallet ID {pallet_id}: No issues detected.")

def process_frame_with_stacking(frame, pallet_id):
    """Detect and draw stacking configurations in a single frame."""
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model(frame_rgb)
    detections = results.pandas().xyxy[0]
    logging.info(f"Number of detections: {len(detections)}")

    # Filter for boxes only
    detections = detections[detections['confidence'] >= model.conf]
    boxes = []
    for _, det in detections.iterrows():
        x1, y1, x2, y2, conf, cls = det[['xmin', 'ymin', 'xmax', 'ymax', 'confidence', 'class']]
        label = model.names[int(cls)].lower()

        if label == "box":
            boxes.append((int(x1), int(y1), int(x2), int(y2)))
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame, f"{label} ({conf:.2f})", (int(x1), int(y1) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Detect stacking issues based on identified boxes
    issues = detect_stacking_issues(boxes)
    for issue in issues:
        log_issue(pallet_id, issue)

    # Store pallet quality result in the pallets table
    store_stacking_result(pallet_id, issues)

    # Display visual indicator if any stacking issues were found
    if issues:
        cv2.putText(frame, "Stacking Issue Detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    return frame, issues

def process_image_with_stacking(image_path, pallet_id):
    """Process a single image file for stacking detection without resizing."""
    frame = cv2.imread(image_path)
    if frame is None:
        logging.error("Image not found.")
        return

    processed_frame, issues = process_frame_with_stacking(frame, pallet_id)
    generate_stacking_report(pallet_id, issues)
    cv2.namedWindow("Image Stacking Detection", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("Image Stacking Detection", processed_frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def process_video_with_stacking(video_path, pallet_id):
    """Process a video file for stacking detection."""
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    frame_skip_interval = 2

    if cap.isOpened():
        cv2.namedWindow("Video Stacking Detection", cv2.WINDOW_NORMAL)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            if frame_count % frame_skip_interval == 0:
                frame_with_stacking, issues = process_frame_with_stacking(frame, pallet_id)
                cv2.imshow("Video Stacking Detection", frame_with_stacking)
                generate_stacking_report(pallet_id, issues)

            frame_count += 1
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

def process_warehouse_with_stacking(video_paths, pallet_id):
    """Process multiple video feeds for warehouse overview with stacking detection."""
    caps = [cv2.VideoCapture(path) for path in video_paths]
    target_width, target_height = 640, 480

    if all(cap.isOpened() for cap in caps):
        cv2.namedWindow("Warehouse Stacking Detection", cv2.WINDOW_NORMAL)
        frame_skip_interval = 2

        while all(cap.isOpened() for cap in caps):
            frames = []
            for cap in caps:
                ret, frame = cap.read()
                if not ret:
                    cap.release()
                    continue
                if int(cap.get(cv2.CAP_PROP_POS_FRAMES)) % frame_skip_interval != 0:
                    continue

                resized_frame = cv2.resize(frame, (target_width, target_height))
                frame_with_stacking, issues = process_frame_with_stacking(resized_frame, pallet_id)
                frames.append(frame_with_stacking)
                generate_stacking_report(pallet_id, issues)

            if len(frames) == 3:
                top_frame = frames[0]
                bottom_frame = np.hstack((frames[1], frames[2]))
                bottom_frame_resized = cv2.resize(bottom_frame, (top_frame.shape[1], target_height))
                combined_frame = np.vstack((top_frame, bottom_frame_resized))
                cv2.imshow("Warehouse Stacking Detection", combined_frame)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        for cap in caps:
            cap.release()
        cv2.destroyAllWindows()
    else:
        logging.error("One or more video paths could not be opened.")

# Main interactive prompt
choice = input("Would you like to scan an image, video, or VIEW ENTIRE WAREHOUSE? (Enter 'image', 'video', or 'warehouse'): ").strip().lower()

if choice == 'image':
    image_path = input("Enter the path of the image file to scan: ").strip()
    pallet_id = int(input("Enter the pallet ID associated with the image: ").strip())
    process_image_with_stacking(image_path, pallet_id)

elif choice == 'video':
    video_path = input("Enter the path of the video file to scan: ").strip()
    pallet_id = int(input("Enter the pallet ID associated with the video: ").strip())
    process_video_with_stacking(video_path, pallet_id)

elif choice == 'warehouse':
    video_paths = [
        r"C:\Users\ethan\Downloads\33.avi",
        r"C:\Users\ethan\Downloads\34.avi",
        r"C:\Users\ethan\Downloads\96.avi"
    ]
    pallet_id = int(input("Enter the pallet ID associated with the warehouse scan: ").strip())
    process_warehouse_with_stacking(video_paths, pallet_id)

else:
    print("Invalid choice. Please enter 'image', 'video', or 'warehouse'.")

# Close the database connection
if conn:
    conn.close()
    logging.info("Processing completed and WMS connection closed.")
