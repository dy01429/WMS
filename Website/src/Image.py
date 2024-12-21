from ultralytics import YOLO
import cv2

# Load the YOLOv8 model (YOLOv8n is the small version, adjust to 'yolov8m', 'yolov8x', etc. for other sizes)
#model = YOLO('yolov8n.pt')  # Replace 'yolov8n.pt' with the desired model version

# Train the model
#model.train(data='C:/Users/dylan/OneDrive/Desktop/Everything/School Work/Fall 2024/Capstone/Test/WMS/data.yaml', epochs=22, imgsz=640)

# Load the two YOLO models
Boxes = YOLO(r'C:\Users\dylan\OneDrive\Desktop\Everything\School Work\Fall 2024\Capstone\Test\WMS\runs\detect\train5\weights\best.pt')
Pallets = YOLO(r'C:\Users\dylan\OneDrive\Desktop\Everything\School Work\Fall 2024\Capstone\Test\WMS\best.pt')

# Load the image
image_path = r'C:\Users\dylan\OneDrive\Desktop\Everything\School Work\Fall 2024\Capstone\Test\WMS\test images\5.jpg'
img = cv2.imread(image_path)

# Object detection with both models
results1 = Boxes(img)
results2 = Pallets(img)

# Access and plot results for both models
annotated_img1 = results1[0].plot()  # Draw the bounding boxes and labels for Boxes
annotated_img2 = results2[0].plot()  # Draw the bounding boxes and labels for Pallets

# Combine the detections from both models
combined_img = cv2.addWeighted(annotated_img1, 0.5, annotated_img2, 0.5, 0)

# Display the combined image with detections from both models
cv2.imshow("YOLOv8 Detection - Combined Models", combined_img)
cv2.waitKey(0)
cv2.destroyAllWindows()