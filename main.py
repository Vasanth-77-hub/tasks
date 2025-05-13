# # BMI Calculator FastAPI Project

# # This project demonstrates a simple BMI calculator implemented as a FastAPI web service.
# # It includes:
# # - FastAPI application setup
# # - Pydantic models for request/response validation
# # - BMI calculation endpoint
# # - HTML template for a simple frontend
# # - Static serving of CSS assets
# # """

# # Import necessary libraries
# from fastapi import FastAPI, Request, Form, HTTPException
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles
# from fastapi.responses import HTMLResponse
# from pydantic import BaseModel, Field, validator
# from typing import Optional
# import uvicorn

# # Create FastAPI app instance
# app = FastAPI(
#     title="BMI Calculator API",
#     description="A simple API to calculate Body Mass Index (BMI)",
#     version="1.0.0"
# )

# # For serving static files (CSS, JS, etc.)
# app.mount("/static", StaticFiles(directory="static"), name="static")

# # Setup Jinja2 templates
# templates = Jinja2Templates(directory="templates")

# # Define Pydantic models for request and response
# class BMIRequest(BaseModel):
#     weight: float = Field(..., gt=0, description="Weight in kilograms")
#     height: float = Field(..., gt=0, description="Height in meters")
    
#     @validator('weight')
#     def validate_weight(cls, v):
#         if v <= 0:
#             raise ValueError("Weight must be positive")
#         if v > 500:  # Reasonable upper limit
#             raise ValueError("Weight seems too high")
#         return v
    
#     @validator('height')
#     def validate_height(cls, v):
#         if v <= 0:
#             raise ValueError("Height must be positive")
#         if v > 3:  # Reasonable upper limit in meters
#             raise ValueError("Height seems too high, please provide in meters")
#         return v

# class BMIResponse(BaseModel):
#     bmi: float
#     category: str
#     weight: float
#     height: float

# # BMI calculation function
# def calculate_bmi(weight: float, height: float) -> tuple:
#     """Calculate BMI and determine category."""
#     bmi = weight / (height ** 2)
    
#     if bmi < 18.5:
#         category = "Underweight"
#     elif 18.5 <= bmi < 25:
#         category = "Normal weight"
#     elif 25 <= bmi < 30:
#         category = "Overweight"
#     else:
#         category = "Obese"
    
#     return bmi, category

# # API Endpoints
# @app.get("/", response_class=HTMLResponse)
# async def home(request: Request):
#     """Serve the main page with BMI calculator form."""
#     return templates.TemplateResponse("index.html", {"request": request})

# @app.post("/calculate", response_model=BMIResponse)
# async def calculate(bmi_request: BMIRequest):
#     """Calculate BMI based on weight and height."""
#     try:
#         bmi, category = calculate_bmi(bmi_request.weight, bmi_request.height)
#         return BMIResponse(
#             bmi=round(bmi, 2),
#             category=category,
#             weight=bmi_request.weight,
#             height=bmi_request.height
#         )
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))

# @app.post("/calculate-form", response_class=HTMLResponse)
# async def calculate_form(
#     request: Request,
#     weight: float = Form(...),
#     height: float = Form(...)
# ):
#     """Handle form submission and render results page."""
#     try:
#         # Validate inputs using the pydantic model
#         bmi_request = BMIRequest(weight=weight, height=height)
#         bmi, category = calculate_bmi(bmi_request.weight, bmi_request.height)
        
#         # Return results page
#         return templates.TemplateResponse(
#             "result.html", 
#             {
#                 "request": request,
#                 "bmi": round(bmi, 2),
#                 "category": category,
#                 "weight": weight,
#                 "height": height
#             }
#         )
#     except ValueError as e:
#         # Return error page
#         return templates.TemplateResponse(
#             "index.html", 
#             {
#                 "request": request,
#                 "error": str(e)
#             }
#         )

# # For running the application directly
# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)



from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator

app = FastAPI()

class BMIRequest(BaseModel):
    weight_kg: float = Field(..., gt=0, lt=500, example=70.5)
    height_cm: float = Field(..., gt=50, lt=300, example=175.0)  

    @field_validator("height_cm")
    def check_height(cls, v):
        if v < 50 or v > 300:
            raise ValueError("Height seems incorrect. Provide height in centimeters.")
        return v

class BMIResponse(BaseModel):
    bmi: float
    category: str

def categorize_bmi(bmi: float) -> str:
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

@app.post("/bmi", response_model=BMIResponse)
def calculate_bmi(data: BMIRequest):
    height_m = data.height_cm / 100
    bmi = data.weight_kg / (height_m ** 2)
    bmi_rounded = round(bmi, 2)
    category = categorize_bmi(bmi_rounded)
    return {"bmi": bmi_rounded, "category": category}
