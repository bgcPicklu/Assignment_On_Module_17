# Assignment_On_Module_17
Assignment: FastAPI and Docker
# Deployment of Bangladeshi Taka Note Detection Model Using REST API & Docker
This project provides a production-ready deployment of a Bangladeshi Taka Note Detection Model using a YOLO (Ultralytics) object detection model, exposed via a FastAPI REST API, and containerized with Docker for easy scalability and deployment.

## Overview

The system allows users to upload an image containing Bangladeshi currency notes and returns:

Detected note types (e.g., 100, 500 Taka)
Confidence scores
Bounding box coordinates

## 📊 Model Info
YOLOv26 trained on Bangladeshi currency dataset

## Technologies Used
FastAPI – High-performance web framework
Ultralytics YOLO – Object detection model
OpenCV – Image processing
Docker & Docker Compose – Containerization
Pydantic – Data validation

## Project Structure
.
├── app/
│   └── main.py                  # FastAPI application
├── model_cls/
│   └── detectionModel.py        # Pydantic schemas
├── pre_trained_model/
│   └── runs/detect/.../best.pt # YOLO trained model
├── temp/                        # Temporary uploaded files
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md

## 🚀 Setup

### Build and Start Container
docker-compose up --build

### Access API
http://localhost:8000/docs

### Curl
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@10_5.jpg;type=image/jpeg'

### Request URL
http://localhost:8000/predict

### Server response
{
  "detections": [
    {
      "class_name": "5",
      "confidence": 0.2938230335712433,
      "bbox": [
        2.713179588317871,
        111.42945861816406,
        219.31390380859375,
        217.2815399169922
      ]
    },
    {
      "class_name": "10",
      "confidence": 0.2752170264720917,
      "bbox": [
        4.219543933868408,
        111.65823364257812,
        217.57424926757812,
        217.40826416015625
      ]
    },
    {
      "class_name": "50",
      "confidence": 0.2668805420398712,
      "bbox": [
        2.713179588317871,
        111.42945861816406,
        219.31390380859375,
        217.2815399169922
      ]
    },
    {
      "class_name": "5",
      "confidence": 0.25059396028518677,
      "bbox": [
        4.727536201477051,
        1.752367615699768,
        218.5460662841797,
        107.66228485107422
      ]
    }
  ]
}

### Response headers
 content-length: 555 
 content-type: application/json 
 date: Wed,15 Apr 2026 16:47:37 GMT 
 server: uvicorn 
### Responses
Code	 Description	Links
200	    Successful Response

### Example Value
Schema
{
  "detections": [
    {
      "class_name": "string",
      "confidence": 0,
      "bbox": [
        0
      ]
    }
  ]
}

## 📡 API Usage

### Endpoint
POST /predict

### Input
- Image file (JPEG/PNG)

### Output
- Detected classes
- Confidence scores
- Bounding boxes