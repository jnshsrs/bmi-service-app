from pydantic import BaseModel, Field

class BMIInput(BaseModel):
    height: float = Field(..., gt=0, description="Height in centimeters")
    weight: float = Field(..., gt=0, description="Weight in kilograms")
