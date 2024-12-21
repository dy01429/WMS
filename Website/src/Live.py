import cv2
from ultralytics import YOLO

# YOLO models
Boxes = YOLO(r'C:\Users\dylan\OneDrive\Desktop\Everything\School Work\Fall 2024\Capstone\Test\WMS\runs\detect\train2\weights\best.pt')
Pallets = YOLO(r'C:\Users\dylan\OneDrive\Desktop\Everything\School Work\Fall 2024\Capstone\Test\WMS\best.pt')

# URLs for each zone
video_zones = {
    'A': 'rtsp://141.165.40.96/stream1',
    'B': 'rtsp://141.165.40.97/stream1',
    'C': 'rtsp://141.165.40.34/stream1',
    'D': 'rtsp://141.165.40.33/stream1',
}

# Let the user select the zone
print("Select a zone to view (A, B, C, D):")
zone = input().upper()

# Check if the input is valid
if zone not in video_zones:
    print(f"Invalid selection: {zone}. Please select a valid zone (A, B, C, D).")
    exit()

# Open live stream for the selected zone
video_path = video_zones[zone]
cap = cv2.VideoCapture(video_path)

# Speed up video by skipping frames
frame_skip = 2
frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1

    # Skip frames to speed up processing
    if frame_count % frame_skip != 0:
        continue

    # Object detection with both models
    results1 = Boxes(frame)
    results2 = Pallets(frame)

    # Access and plot results for both models
    annotated_frame1 = results1[0].plot()
    annotated_frame2 = results2[0].plot()

    # Combine the detections from both models
    combined_frame = cv2.addWeighted(annotated_frame1, 0.5, annotated_frame2, 0.5, 0)

    # Resize the frame for display
    resized_frame = cv2.resize(combined_frame, (1000, 800))

    # Add zone label text
    text = f"Zone {zone} - Live Stream"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
    text_x = (resized_frame.shape[1] - text_size[0]) // 2
    text_y = 40
    cv2.putText(resized_frame, text, (text_x, text_y), font, font_scale, (255, 255, 255), font_thickness, cv2.LINE_AA)

    # Display live footage with detections
    cv2.imshow(f"YOLOv8 Detection - Zone {zone}", resized_frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):  # Press 'q' to exit the loop
        break

cap.release()
cv2.destroyAllWindows()
