import cv2
import torch
import mysql.connector
from datetime import datetime
import logging
import numpy as np
from ultralytics import YOLO

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Load YOLOv8 model
custom_model_path = r'C:\Users\dylan\OneDrive\Desktop\Everything\School Work\Fall 2024\Capstone\Test\WMS\runs\detect\train2\weights\best.pt'
model = YOLO(custom_model_path)
logging.info("Custom YOLOv8 model loaded successfully")

# Set confidence and IoU thresholds
model.conf = 0.5  # Confidence threshold
model.iou = 0.3  # IoU threshold

# Connect to the MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password="w+XdW6dnK8L_GP5",
    database='capstone'
)
cursor = conn.cursor()

# Improved resolution
target_width, target_height = 1280, 720  # Increased resolution for better clarity


def calculate_iou(box1, box2):
    """Calculate IoU (Intersection over Union) between two bounding boxes."""
    x1, y1, x2, y2 = box1
    x1_p, y1_p, x2_p, y2_p = box2

    inter_x1 = max(x1, x1_p)
    inter_y1 = max(y1, y1_p)
    inter_x2 = min(x2, x2_p)
    inter_y2 = min(y2, y2_p)
    inter_area = max(0, inter_x2 - inter_x1) * max(0, inter_y2 - inter_y1)

    area1 = (x2 - x1) * (y2 - y1)
    area2 = (x2_p - x1_p) * (y2_p - y1_p)
    union_area = area1 + area2 - inter_area

    return inter_area / union_area if union_area > 0 else 0


def resize_frame(frame):
    """Resize frame to the target dimensions."""
    return cv2.resize(frame, (target_width, target_height))


def log_detection_to_wms(label, width, height, client_id):
    """Logs detected boxes into the WMS database."""
    cursor.execute("SELECT client_id, client_name FROM clients WHERE client_id = %s", (client_id,))
    client_record = cursor.fetchone()

    if not client_record:
        cursor.execute('''
            INSERT INTO clients (client_name, client_address, contact_details) 
            VALUES ('Default Client', '123 Main St', 'contact@example.com')
        ''')
        conn.commit()
        client_id = cursor.lastrowid
        client_name = 'Default Client'
        logging.info(f"Default client added with ID {client_id}.")
    else:
        client_name = client_record[1]

    base_label = client_name.replace(" ", "").lower()
    cursor.execute("SELECT COUNT(*) + 1 FROM boxes WHERE box_label LIKE %s", (base_label + '%',))
    next_number = cursor.fetchone()[0]
    unique_label = f"{base_label}{next_number}"

    cursor.execute('''
        INSERT INTO boxes (box_label, length, width, height, weight)
        VALUES (%s, %s, %s, %s, %s)
    ''', (unique_label, width, height, height, 1.0))
    conn.commit()
    box_id = cursor.lastrowid

    cursor.execute('''
        INSERT INTO inventory (client_id, description, quantity, box_id)
        VALUES (%s, %s, %s, %s)
    ''', (client_id, f"{unique_label} {width}x{height}", 1, box_id))
    conn.commit()
    logging.info(f"Box '{unique_label}' linked to inventory with client ID {client_id}.")


# Video paths
video_paths = [
    r'C:\Users\dylan\OneDrive\Desktop\Everything\School Work\Fall 2024\Capstone\Test\WMS\test videos\Zones\33.avi',
    r'C:\Users\dylan\OneDrive\Desktop\Everything\School Work\Fall 2024\Capstone\Test\WMS\test videos\Zones\34.avi',
    r'C:\Users\dylan\OneDrive\Desktop\Everything\School Work\Fall 2024\Capstone\Test\WMS\test videos\Zones\96.avi'
]

choice = input(
    "Would you like to scan an image, video, or VIEW ENTIRE WAREHOUSE? (Enter 'image', 'video', or 'warehouse'): ").strip().lower()

if choice == 'image':
    file_path = input("Enter the path of the image file to scan: ").strip()
    frame = cv2.imread(file_path)
    if frame is not None:
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Perform inference
        results = model(frame_rgb, conf=model.conf, iou=model.iou, imgsz=1920)

        if len(results) > 0:
            result = results[0]
            detections = result.boxes
            class_names = model.names

            # Extract detections
            xyxys = detections.xyxy.cpu().numpy()  # N x 4
            confs = detections.conf.cpu().numpy()  # N
            classes = detections.cls.cpu().numpy().astype(int)  # N

            for (x1, y1, x2, y2), conf, cls_id in zip(xyxys, confs, classes):
                label = class_names[cls_id].lower()
                if conf >= model.conf and label == "box":
                    # Ensure bounding box within frame bounds
                    x1, y1, x2, y2 = max(int(x1), 0), max(int(y1), 0), min(int(x2), frame.shape[1]), min(int(y2),
                                                                                                         frame.shape[0])
                    width, height = x2 - x1, y2 - y1
                    log_detection_to_wms(label, width, height, client_id=1)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, f"Box ({width}x{height})", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (0, 255, 0), 2)

        cv2.imshow("Image Detection", frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

elif choice == 'warehouse':
    caps = [cv2.VideoCapture(path) for path in video_paths]
    if all(cap.isOpened() for cap in caps):
        cv2.namedWindow("Warehouse Overview", cv2.WINDOW_NORMAL)
        frame_skip_interval = 2  # Skip every 2 frames for faster processing

        while all(cap.isOpened() for cap in caps):
            frames = []
            for cap in caps:
                ret, frame = cap.read()
                if not ret:
                    cap.release()
                    continue
                if int(cap.get(cv2.CAP_PROP_POS_FRAMES)) % frame_skip_interval != 0:
                    continue  # Skip frames for speed
                frame = resize_frame(frame)  # Resize to target resolution
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Perform inference
                results = model(frame_rgb, conf=model.conf, iou=model.iou, imgsz=1920)
                if len(results) > 0:
                    result = results[0]
                    detections = result.boxes
                    class_names = model.names

                    xyxys = detections.xyxy.cpu().numpy()
                    confs = detections.conf.cpu().numpy()
                    classes = detections.cls.cpu().numpy().astype(int)

                    for (x1, y1, x2, y2), conf, cls_id in zip(xyxys, confs, classes):
                        label = class_names[cls_id].lower()
                        if conf >= model.conf and label == "box":
                            x1, y1, x2, y2 = max(int(x1), 0), max(int(y1), 0), min(int(x2), frame.shape[1]), min(
                                int(y2), frame.shape[0])
                            width, height = x2 - x1, y2 - y1
                            log_detection_to_wms(label, width, height, client_id=1)
                            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                            cv2.putText(frame, f"Box ({width}x{height})", (x1, y1 - 10),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                frames.append(frame)

            # Align widths of all frames for vertical stacking
            if len(frames) == 3:
                top_frame = resize_frame(frames[0])  # Resize top frame
                bottom_frames = [resize_frame(frames[1]), resize_frame(frames[2])]
                bottom_frame = np.hstack(bottom_frames)  # Stack bottom two frames horizontally

                # Ensure consistent width for vertical stacking
                bottom_frame_resized = cv2.resize(bottom_frame, (target_width, bottom_frame.shape[0]))
                combined_frame = np.vstack((top_frame, bottom_frame_resized))

                cv2.imshow("Warehouse Overview", combined_frame)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        for cap in caps:
            cap.release()
        cv2.destroyAllWindows()

elif choice == 'video':
    file_path = input("Enter the path of the video file to scan: ").strip()
    cap = cv2.VideoCapture(file_path)
    tracked_boxes = {}
    frame_skip_interval = 2  # Faster video processing by skipping frames
    frame_count = 0

    if cap.isOpened():
        cv2.namedWindow("Box and Pallet Detection", cv2.WINDOW_NORMAL)

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                logging.info("End of video.")
                break

            if frame_count % frame_skip_interval == 0:
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # Perform inference
                results = model(frame_rgb, conf=model.conf, iou=model.iou, imgsz=1920)
                if len(results) > 0:
                    result = results[0]
                    detections = result.boxes
                    class_names = model.names

                    xyxys = detections.xyxy.cpu().numpy()
                    confs = detections.conf.cpu().numpy()
                    classes = detections.cls.cpu().numpy().astype(int)

                    current_frame_boxes = {}

                    for (x1, y1, x2, y2), conf, cls_id in zip(xyxys, confs, classes):
                        label = class_names[cls_id].lower()
                        if conf >= model.conf and label == "box":
                            x1, y1, x2, y2 = max(int(x1), 0), max(int(y1), 0), min(int(x2), frame.shape[1]), min(
                                int(y2), frame.shape[0])
                            new_box = (x1, y1, x2, y2)
                            width, height = x2 - x1, y2 - y1

                            # Check duplicates using IoU
                            is_duplicate = False
                            for tracked_box in tracked_boxes.values():
                                if calculate_iou(new_box, tracked_box) > 0.5:
                                    is_duplicate = True
                                    break

                            if not is_duplicate:
                                box_id = f"{x1}_{y1}"
                                tracked_boxes[box_id] = new_box
                                log_detection_to_wms(label, width, height, client_id=1)

                                color = (0, 255, 0)
                                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                                cv2.putText(frame, f"Box ({width}x{height})", (x1, y1 - 10),
                                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                                cv2.putText(frame, f"Conf: {conf:.2f}", (x1, y2 + 20),
                                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

            # Draw tracked boxes
            for box_coords in tracked_boxes.values():
                x1, y1, x2, y2 = box_coords
                width = x2 - x1
                height = y2 - y1
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f"Box ({width}x{height})", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            cv2.imshow('Box and Pallet Detection', frame)
            frame_count += 1

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
else:
    print("Invalid choice. Please enter 'image', 'video', or 'warehouse'.")

conn.close()
logging.info("Processing completed and WMS connection closed.")
