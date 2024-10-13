from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_bmi_valid():
    response = client.get("/bmi/175-70")
    assert response.status_code == 200
    assert response.json() == {"BMI": 22.86}

def test_bmi_invalid_format():
    response = client.get("/bmi/175x70")
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid input format. Use height-weight as float values."}

def test_bmi_non_numeric_values():
    response = client.get("/bmi/abc-def")
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid input format. Use height-weight as float values."}
