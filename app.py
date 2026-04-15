from fastapi import FastAPI, File, UploadFile, HTTPException
import shutil
import os
# import torch
from ultralytics import YOLO
import cv2

app = FastAPI()

# Load model once
# model = torch.hub.load('ultralytics/yolo26n', 'custom', path=r'E:/Test/Per/Online Course/Ostad/Assignments/Assignment on Module 16/runs/detect/Bangladesh_Currency_Notes/weights/best.pt',force_reload=True)
model = YOLO(r"E:/Test/Per/Online Course/Ostad/Assignments/Assignment on Module 16/runs/detect/Bangladesh_Currency_Notes/weights/best.pt")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Invalid file type")

    file_path = f"temp/{file.filename}"

    os.makedirs("temp", exist_ok=True)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    img = cv2.imread(file_path)

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

    return {"detections": detections}