from pydantic import BaseModel, Field

class HeightWeight(BaseModel):
    height: float = Field(..., gt=0, lt=250, description="Height in centimeters")
    weight: float = Field(..., gt=0, lt=300, description="Weight in kilograms")
