import cv2
from pyzbar.pyzbar import decode
import mysql.connector
from datetime import datetime
from ultralytics import YOLO

# Define maximum box size
MAX_BOX_WIDTH = 1300
MAX_BOX_HEIGHT = 1300

# Database connection function
def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password="w+XdW6dnK8L_GP5",
        database='capstone'
    )

# YOLO model initialization
Boxes = YOLO(r'C:\Users\dylan\OneDrive\Desktop\Everything\School Work\Fall 2024\Capstone\Test\WMS\runs\detect\train2\weights\best.pt')

# Mapping zones to video file paths
video_zones = {
    'A': r'C:\Users\dylan\OneDrive\Desktop\Everything\School Work\Fall 2024\Capstone\Test\WMS\test videos\Zones\96.avi',
    'B': r'C:\Users\dylan\OneDrive\Desktop\Everything\School Work\Fall 2024\Capstone\Test\WMS\test videos\Zones\97.avi',
    'C': r'C:\Users\dylan\OneDrive\Desktop\Everything\School Work\Fall 2024\Capstone\Test\WMS\test videos\Zones\34.avi',
    'D': r'C:\Users\dylan\OneDrive\Desktop\Everything\School Work\Fall 2024\Capstone\Test\WMS\test videos\Zones\33.avi',
}

# Function to retrieve or update zone information
def manage_zone(barcodedata, cursor, conn):
    query = "SELECT zone FROM barcode_scans WHERE barcode_data = %s ORDER BY scan_time DESC LIMIT 1"
    cursor.execute(query, (barcodedata,))
    result = cursor.fetchone()
    if result:
        current_zone = result[0]
        print(f"Barcode {barcodedata} found in Zone {current_zone}.")
        action = input("Enter '1' to view this zone or '2' to change the zone: ").strip()
        if action == '2':
            current_zone = assign_zone_to_barcode(barcodedata, cursor, conn)
    else:
        print(f"Barcode {barcodedata} not found in the database.")
        current_zone = assign_zone_to_barcode(barcodedata, cursor, conn)
    return current_zone

# Function to assign zone to barcode
def assign_zone_to_barcode(barcodedata, cursor, conn):
    print("Available zones: A, B, C, D")
    while True:
        zone = input("Please assign a zone to this barcode (A, B, C, D): ").strip().upper()
        if zone in video_zones.keys():
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            query = "INSERT INTO barcode_scans (barcode_data, scan_time, zone) VALUES (%s, %s, %s)"
            cursor.execute(query, (barcodedata, timestamp, zone))
            conn.commit()
            print(f"Zone {zone} assigned to barcode {barcodedata}.")
            return zone
        else:
            print("Invalid zone. Please enter A, B, C, or D.")

# Function to display zone video with YOLO detections
def display_zone_video(zone, barcode_name):
    video_path = video_zones.get(zone)
    if not video_path:
        print(f"No video path found for Zone {zone}.")
        return

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video for Zone {zone}.")
        return

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = Boxes(frame)
        boxes = results[0].boxes
        annotated_frame = frame.copy()

        # Draw boxes and add barcode name above it
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            width, height = x2 - x1, y2 - y1
            if width <= MAX_BOX_WIDTH and height <= MAX_BOX_HEIGHT:
                cv2.rectangle(annotated_frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                # Add the barcode name above the box with green color and larger font
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(annotated_frame, barcode_name, (int(x1), int(y1)-10), font, 1.5, (0, 255, 0), 3, cv2.LINE_AA)

        # Resize and add the zone name in the center
        resized_frame = cv2.resize(annotated_frame, (1000, 800))
        font = cv2.FONT_HERSHEY_SIMPLEX
        text_size = cv2.getTextSize(f"Zone {zone}", font, 1, 2)[0]
        text_x = (resized_frame.shape[1] - text_size[0]) // 2
        cv2.putText(resized_frame, f"Zone {zone}", (text_x, 50), font, 1, (255, 255, 255), 2)

        cv2.imshow(f"Zone {zone}", resized_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Main function
def main():
    conn = connect_db()
    cursor = conn.cursor()
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        barcodes = decode(frame)
        for barcode in barcodes:
            barcodedata = barcode.data.decode('utf-8')
            print(f"Detected barcode: {barcodedata}")
            zone = manage_zone(barcodedata, cursor, conn)
            display_zone_video(zone, barcodedata)  # Pass the barcode name to display

        cv2.imshow("Barcode Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    conn.close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
