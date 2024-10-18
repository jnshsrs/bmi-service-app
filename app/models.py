from pydantic import BaseModel, Field

class BMIInput(BaseModel):
    height: float = Field(..., default=170, gt=0, lt=250, description="Height in centimeters")
    weight: float = Field(..., default=80, gt=0, lt=300, description="Weight in kilograms")
