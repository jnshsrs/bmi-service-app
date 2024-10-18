from fastapi import FastAPI, HTTPException
from app.models import HeightWeight
from fastapi import Body

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the BMI calculator!"}

@app.post("/bmi")
def calculate_bmi(bmi_input: HeightWeight = Body(...)):
    """
    Calculate the Body Mass Index (BMI) based on the provided height and weight.
    """
    try:
        # Validate the input using Pydantic model
        bmi_input = HeightWeight(height=bmi_input.height, weight=bmi_input.weight)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Calculate BMI
    height_in_meters = bmi_input.height / 100  # Convert height from cm to meters
    bmi = bmi_input.weight / (height_in_meters ** 2)
    return {"BMI": round(bmi, 2)}

@app.get("/health")
def health_check():
    """
    Health check endpoint to verify the service status.
    """
    return {"status": "healthy"}