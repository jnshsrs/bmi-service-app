from fastapi import FastAPI, HTTPException
from app.models import BMIInput

app = FastAPI()

@app.get("/bmi/{height_weight}")
def calculate_bmi(height_weight: str):
    try:
        # Split the height and weight from the URL string (formatted as height-weight)
        height, weight = map(float, height_weight.split("-"))
        # Use Pydantic model for validation
        bmi_input = BMIInput(height=height, weight=weight)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid input format. Use height-weight as float values.")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Calculate BMI
    height_in_meters = bmi_input.height / 100  # Convert height from cm to meters
    bmi = bmi_input.weight / (height_in_meters ** 2)
    return {"BMI": round(bmi, 2)}

@app.get("/health")
def health_check():
    return {"status": "healthy"}