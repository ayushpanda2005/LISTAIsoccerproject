# from ultralytics import YOLO
# import cv2

# # Load the trained YOLOv8 model
# model = YOLO(r"C:\Users\Arctic-LianLi\OneDrive\Desktop\cv\yolovobjectdetectiontutorial\runs\detect\train5\weights\yolov11_custom.pt")

# # Run prediction
# results = model.predict(
#     source=r"C:\Users\Arctic-LianLi\OneDrive\Desktop\cv\yolovobjectdetectiontutorial\val\images\d1.png",
#     show=False,  # we handle showing manually
#     save=False,
#     # conf=0.5
# )

# # Display with OpenCV until a key is pressed
# for r in results:
#     img = r.plot()  # draw predictions
#     cv2.imshow("Prediction", img)
#     cv2.waitKey(0)  # wait for key press
#     cv2.destroyAllWindows()
from ultralytics import YOLO
import cv2

# Load the trained model
model = YOLO(r"C:\Users\Arctic-LianLi\OneDrive\Desktop\cv\yolovobjectdetectiontutorial\runs\detect\train5\weights\yolov11_custom.pt")

# Path to your video file
video_path = r"C:\Users\Arctic-LianLi\OneDrive\Desktop\cv\yolovobjectdetectiontutorial\traffic_lights.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Predict on frame
    results = model.predict(source=frame, show=False, save=False, stream=False)

    for r in results:
        annotated = r.plot()
        cv2.imshow("YOLOv8 Half Speed Video", annotated)

    # Half-speed playback: ~66ms delay (~15 FPS)
    if cv2.waitKey(66) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

