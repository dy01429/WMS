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

# Retrieve the last known zone for a barcode
def get_last_zone(barcodedata, cursor):
    query = "SELECT zone FROM barcode_scans WHERE barcode_data = %s ORDER BY scan_time DESC LIMIT 1"
    cursor.execute(query, (barcodedata,))
    result = cursor.fetchone()
    if result:
        return result[0]
    return None

# Insert a new zone scan for a barcode
def insert_zone_scan(barcodedata, zone, cursor, conn):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    query = "INSERT INTO barcode_scans (barcode_data, scan_time, zone) VALUES (%s, %s, %s)"
    cursor.execute(query, (barcodedata, timestamp, zone))
    conn.commit()

# Determine zone from coordinates
def get_zone_from_coordinates(x_center, y_center, frame_width, frame_height):
    half_width = frame_width / 2
    half_height = frame_height / 2
    if x_center < half_width and y_center < half_height:
        return 'A'
    elif x_center >= half_width and y_center < half_height:
        return 'B'
    elif x_center < half_width and y_center >= half_height:
        return 'C'
    else:
        return 'D'

# Draw grid on the frame
def draw_grid(frame):
    height, width, _ = frame.shape
    step_x = width // 2
    step_y = height // 2

    # Draw grid lines
    for x in range(1, 2):
        cv2.line(frame, (x * step_x, 0), (x * step_x, height), (255, 0, 0), 2)
    for y in range(1, 2):
        cv2.line(frame, (0, y * step_y), (width, y * step_y), (255, 0, 0), 2)

    # Add zone labels
    font = cv2.FONT_HERSHEY_SIMPLEX
    zones = ['Zone A', 'Zone B', 'Zone C', 'Zone D']
    for i, label in enumerate(zones):
        col = i % 2
        row = i // 2
        x = col * step_x + 10
        y = (row + 1) * step_y - 10
        cv2.putText(frame, label, (x, y), font, 1, (255, 0, 0), 2, cv2.LINE_AA)

    return frame

# Display zone footage with YOLO detections
def display_zone_video(barcodedata, zone, cursor, conn):
    video_path = video_zones.get(zone)
    if not video_path:
        print(f"No video found for Zone {zone}.")
        return

    cap = cv2.VideoCapture(video_path)
    last_zone = zone

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Draw grid on the footage
        frame = draw_grid(frame)

        # YOLO detections
        results = Boxes(frame)
        for box in results[0].boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            width_box, height_box = x2 - x1, y2 - y1

            # Enforce maximum box size
            if width_box > MAX_BOX_WIDTH or height_box > MAX_BOX_HEIGHT:
                continue

            x_center = (x1 + x2) / 2
            y_center = (y1 + y2) / 2
            new_zone = get_zone_from_coordinates(x_center, y_center, frame.shape[1], frame.shape[0])

            # Draw green bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            # Annotate with barcode data
            cv2.putText(frame, f"Barcode: {barcodedata}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

            # Handle zone change
            if new_zone != last_zone:
                print(f"Object linked to Barcode {barcodedata} moved to new zone: {new_zone}. Updating database...")
                insert_zone_scan(barcodedata, new_zone, cursor, conn)
                last_zone = new_zone

        # After all annotations are done, we consider frame as annotated_frame
        annotated_frame = frame

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

        # Barcode detection
        barcodes = decode(frame)
        for barcode in barcodes:
            barcodedata = barcode.data.decode('utf-8')
            last_zone = get_last_zone(barcodedata, cursor)

            if last_zone:
                print(f"Barcode {barcodedata} found in Zone {last_zone}.")
                # Give user options when barcode is found
                while True:
                    choice = input("Enter '1' to view zone footage or '2' to change barcode zone: ").strip()
                    if choice == '1':
                        # View zone footage
                        display_zone_video(barcodedata, last_zone, cursor, conn)
                        break
                    elif choice == '2':
                        # Change barcode zone
                        while True:
                            new_zone = input("Enter a new a zone (A,B,C,D): ").strip().upper()
                            if new_zone in video_zones:
                                insert_zone_scan(barcodedata, new_zone, cursor, conn)
                                print(f"Assigned Zone {new_zone} to Barcode {barcodedata}.")
                                display_zone_video(barcodedata, new_zone, cursor, conn)
                                break
                            else:
                                print("Invalid input. Please enter a valid zone (A,B,C,D):")
                        break
                    else:
                        print("Invalid choice. Please enter '1' or '2'.")
            else:
                # If barcode not in database, assign a zone
                print(f"Barcode {barcodedata} not found. Please enter a valid zone (A,B,C,D):")
                while True:
                    zone = input("Please give barcode a zone (A,B,C,D): ").strip().upper()
                    if zone in video_zones:
                        insert_zone_scan(barcodedata, zone, cursor, conn)
                        print(f"Assigned Zone {zone} to Barcode {barcodedata}.")
                        display_zone_video(barcodedata, zone, cursor, conn)
                        break
                    else:
                        print("Invalid input. Please give barcode a zone (A,B,C,D): ")

        # Resize the barcode scanner
        resized_frame = cv2.resize(frame, (700, 700))
        cv2.imshow("Barcode Scanner", resized_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    conn.close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()