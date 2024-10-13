# BMI API Service

This project provides a simple REST API to calculate the Body Mass Index (BMI) using **FastAPI**. The BMI is calculated based on the user's height and weight provided via a URL.

## Features
- **BMI Calculation**: Calculates BMI based on height and weight.
- **Pydantic Validation**: Uses Pydantic for input validation.
- **FastAPI**: The API is built with FastAPI for high performance.
- **Docker**: The service is containerized using Docker.
- **GitHub Actions CI/CD**: Automatically deploys to Azure App Service upon push to the `main` branch.

## Endpoints

### Calculate BMI
- **GET** `/bmi/{height-weight}`
  - Example: `/bmi/175-70` calculates BMI for a height of 175 cm and weight of 70 kg.
  
  **Response**:
  ```json
  {
    "BMI": 22.86
  }
  ```

## Local Setup

### Prerequisites
- **Python 3.11**
- **Docker**
- **Azure CLI**

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/bmi-api-service.git
cd bmi-api-service
```

### Step 2: Set Up Virtual Environment
```bash
python3.11 -m venv bmi-api-env
source bmi-api-env/bin/activate  # On Windows, use bmi-api-env\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application Locally
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Docker Setup

### Build and Run Docker Image
To build and run the Docker container locally:
```bash
docker build -t bmi-api-service .
docker run -p 8000:8000 bmi-api-service
```

You can access the API at `http://localhost:8000`.

## Deployment

This project uses **GitHub Actions** for CI/CD to automatically build the Docker image and deploy it to **Azure App Service** when pushing to the `main` branch.

### Prerequisites for Deployment:
- **Azure App Service** and **Azure Container Registry (ACR)** credentials.
- Set up GitHub Secrets:
  - `AZURE_CREDENTIALS`: Azure service principal credentials.
  - `ACR_USERNAME`: Azure Container Registry username.
  - `ACR_PASSWORD`: Azure Container Registry password.

### Steps:
1. Push code to the `main` branch.
2. GitHub Actions will:
   - Build the Docker image.
   - Push the image to Azure Container Registry (ACR).
   - Deploy the image to Azure App Service.

### Infrastructure as Code:
The first push to the `main` branch will create the necessary Azure infrastructure (App Service, ACR, Resource Group) if it doesn’t already exist.

## Running Tests

To run the test suite, ensure you're in the project root and your virtual environment is activated, then run:
```bash
pytest tests/test_bmi.py
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
