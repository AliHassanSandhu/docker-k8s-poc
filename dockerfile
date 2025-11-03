# Use lightweight base image
FROM python:3.12

# Set working directory
WORKDIR /app

# Install dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY app/ .

# Health check command for Docker
HEALTHCHECK CMD curl --fail http://localhost:8000/ || exit 1

# Run FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
