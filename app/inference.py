import cv2
from ultralytics import YOLO
from model_cls.detectionModel import Detection

model = YOLO("pre_trained_model/runs/detect/Bangladesh_Currency_Notes/weights/best.pt")

def run_inference(image_path):
    img = cv2.imread(image_path)

    results = model(img)

    detections = []

    for box in results[0].boxes:
        detections.append(
            Detection(
                class_name=model.names[int(box.cls)],
                confidence=float(box.conf),
                bbox=box.xyxy[0].tolist()
            )
        )

    return detections


if __name__ == "__main__":
    output = run_inference("test.jpg")
    for det in output:
        print(det.json())