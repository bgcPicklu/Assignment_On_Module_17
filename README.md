# Assignment_On_Module_17
Assignment: FastAPI and Docker
# Bangladeshi Taka Note Detection API

## 🚀 Setup

### Build Docker Image
docker build -t taka-detection-api .

### Run Container
docker run -p 8000:8000 taka-detection-api

## 📡 API Usage

### Endpoint
POST /predict

### Input
- Image file (JPEG/PNG)

### Output
- Detected classes
- Confidence scores
- Bounding boxes

## 🧪 Example
curl -X POST "http://localhost:8000/predict" -F "file=@test.jpg"

## 📁 Project Structure
(Explain folder structure)

## 📊 Model Info
YOLOv26 trained on Bangladeshi currency dataset