from fastapi import FastAPI, File, UploadFile, HTTPException
import shutil
import os
import cv2
from ultralytics import YOLO

from model_cls.detectionModel import Detection, PredictionResponse

app = FastAPI(title="YOLO Detection API")

# Load model once at startup
model = YOLO("trained_model/runs/detect/Bangladesh_Currency_Notes/weights/best.pt")

@app.post("/predict", response_model=PredictionResponse)
async def predict(file: UploadFile = File(...)):
    
    # Validate file type
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Invalid file type")

    # Save uploaded file
    os.makedirs("temp", exist_ok=True)
    file_path = os.path.join("temp", file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Read image
    img = cv2.imread(file_path)

    if img is None:
        raise HTTPException(status_code=400, detail="Invalid image file")

    # Run inference
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

    return PredictionResponse(detections=detections)