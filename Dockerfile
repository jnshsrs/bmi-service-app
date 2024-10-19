# Use Python slim image as base
FROM python:3.11-bullseye

# Set the working directory inside the container
WORKDIR /app

RUN apt-get update
RUN apt-get install -y curl

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port FastAPI will run on
EXPOSE 8000

# Run the FastAPI app using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
