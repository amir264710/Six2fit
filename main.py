from fastapi import FastAPI
from database import engine
import models
from routers import clients, get_plan
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials


# Create tables if they don't exist
models.Base.metadata.create_all(bind=engine)
security = HTTPBasic()

# Initialize FastAPI app with more metadata
app = FastAPI(
    title="Six2fit API",
    description="A FastAPI-based system for manage client and meal plan micro service.",
    version="0.0.1",
    terms_of_service="https://six2fit.com/?wmc-currency=IRT",
    contact={
        "name": "Support Team",
        "url": "https://six2fit.com/?wmc-currency=IRT",
        "email": "info@six2fit.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    }
)

# Include routes
app.include_router(clients.router)
app.include_router(get_plan.router, prefix="/files", tags=["files"])

@app.get("/")
def read_root(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = "admin"
    correct_password = "secret"

    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"message": f"Hello, {credentials.username}!"}
