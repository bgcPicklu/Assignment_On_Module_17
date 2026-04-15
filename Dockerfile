# Define python official image to install in docker environment
From python:3.10.20

# set/create working directory
WORKDIR /app

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# copy requirements and install dependencies as per requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copy full project (i.e. app & model_cls)
COPY app/ ./app/
COPY model_cls/ ./model_cls/
COPY trained_model/ ./trained_model/

# Add pythonpath to include the /app directory
ENV PYTHONPATH=/app

# Expose port
EXPOSE 8000

# Update entrypoint to use uvicorn for ASGI apps
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]