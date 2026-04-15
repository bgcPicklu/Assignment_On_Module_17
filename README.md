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
![alt text](image-7.png)

## 🚀 Setup
### Build and Start Container
docker-compose up --build

### Access API
http://localhost:8000/docs

### Curl
![alt text](image-1.png)

### Request URL
![alt text](image-2.png)

### Server response
![alt text](image-3.png)

### Response headers
![alt text](image-6.png)

## 📡 API Usage

### Endpoint
POST /predict

### Input
- Image file (JPEG/PNG)

### Output
- Detected classes
- Confidence scores
- Bounding boxes