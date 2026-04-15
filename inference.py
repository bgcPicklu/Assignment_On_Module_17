# import torch
from ultralytics import YOLO
import cv2

# Load model (adjust path)
# model = torch.hub.load('ultralytics/yolo26n', 'custom', path=r'E:/Test/Per/Online Course/Ostad/Assignments/Assignment on Module 16/runs/detect/Bangladesh_Currency_Notes/weights/best.pt',force_reload=True)
model = YOLO(r"E:/Test/Per/Online Course/Ostad/Assignments/Assignment on Module 16/runs/detect/Bangladesh_Currency_Notes/weights/best.pt")

def run_inference(image_path):
    img = cv2.imread(image_path)

    # Run inference
    results = model(img)

    detections = []

    # for *box, conf, cls in results.xyxy[0]:
    #     detections.append({
    #         "class": model.names[int(cls)],
    #         "confidence": float(conf),
    #         "bbox": [float(x) for x in box]
    #     })

    for box in results[0].boxes:
        detections.append({
            "class": model.names[int(box.cls)],
            "confidence": float(box.conf),
            "bbox": box.xyxy[0].tolist()
        })

    return detections

if __name__ == "__main__":
    output = run_inference("test.jpg")
    print(output)