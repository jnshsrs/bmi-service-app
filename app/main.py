from fastapi import FastAPI, HTTPException
from app.models import BMIInput
from fastapi import Body

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the BMI calculator!"}

@app.post("/bmi")
def calculate_bmi(bmi_input: BMIInput = Body(...)):
    try:
        # Validate the input using Pydantic model
        bmi_input = BMIInput(height=bmi_input.height, weight=bmi_input.weight)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Calculate BMI
    height_in_meters = bmi_input.height / 100  # Convert height from cm to meters
    bmi = bmi_input.weight / (height_in_meters ** 2)
    return {"BMI": round(bmi, 2)}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/bmi")
def bmi_info():
    return {"Info": "Use BMI calculator by sending a GET request to /bmi/{height}-{weight} endpoint."}