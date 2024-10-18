# Use the official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . .

# Install curl for health check
RUN apt-get update && apt-get install -y curl

# Expose the port FastAPI will run on
EXPOSE 8000

# Health check to ping the /health endpoint
HEALTHCHECK CMD curl --fail --output /dev/null --silent http://localhost:8000/health

# Command to run the FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
