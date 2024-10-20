from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_bmi_valid():
    # Assuming your API endpoint is POST /bmi and expects JSON payload for height and weight
    response = client.post(
        "/bmi",
        json={"height": 175, "weight": 70}  # Provide the same data as in your API call
    )
    
    assert response.status_code == 200
    # Adjust the BMI calculation based on your backend logic
    assert response.json() == {"BMI": 22.86}

def test_version():
    # Assuming your API endpoint is POST /bmi and expects JSON payload for height and weight
    response = client.get("/version")
    assert response.status_code == 200