import cv2
from ultralytics import YOLO
import pandas as pd  # Certifique-se de que pandas está instalado

# Load a pretrained model
model = YOLO("yolov8n.pt")  # Certifique-se de que este é o caminho correto para o seu modelo

# Open the video
cap = cv2.VideoCapture("mp4/pov-video.mp4")

# Check if video opened successfully
if not cap.isOpened():
    print("Erro ao abrir o vídeo.")
    exit()

# Process each frame of the video
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Perform object detection on the frame
    results = model(frame)

    # Process the results (draw boxes and labels)
    for result in results:
        for box in result.boxes:
            x_min, y_min, x_max, y_max = box.xyxy[0]
            conf = box.conf[0]
            class_id = box.cls[0]
            name = model.names[int(class_id)]
            cv2.rectangle(frame, (int(x_min), int(y_min)), (int(x_max), int(y_max)), (0, 255, 0), 2)
            cv2.putText(frame, name, (int(x_min), int(y_min) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # Display the frame with detections
    cv2.imshow("Video with Detections", frame)

    # Exit loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()