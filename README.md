# Six2fit

a platform for design meal plan based on the client preference with help of open ai latest models. 

![image](https://github.com/user-attachments/assets/364661ae-8700-4730-9307-e5e8d80710a5)

# Six2fit API

## Overview
Six2fit API is a FastAPI-based system for managing client data and meal plans as a microservice. It uses PostgreSQL as the database and SQLAlchemy as the ORM.

## Features
- User authentication using HTTP Basic Authentication
- CRUD operations for managing clients
- Secure file retrieval for meal plans
- PostgreSQL integration using SQLAlchemy
- Modular routing with FastAPI

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- PostgreSQL
- Virtual environment (optional but recommended)

### Clone the Repository
```bash
git clone repo
cd six2fit-api
```

### Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies
the req file is under development
```bash
pip install -r requirements.txt
```

## Configuration
Modify `DATABASE_URL` in `database.py` to match your PostgreSQL credentials:
```python
DATABASE_URL= "postgresql://username:password@localhost/dbname"
```

## Running the Application
```bash
uvicorn main:app --reload
```
The API will be accessible at: [http://65.109.197.142:8000](http:/65.109.197.142:8000)

## API Endpoints
### Authentication
- **GET /**: Root endpoint with HTTP Basic Authentication.

### Clients
- **POST /clients/**: Add a new client.

### File Handling
- **GET /files/getfile/{filename}**: Retrieve a meal plan file.

## Database Models
The database consists of a `clients` table with attributes such as:
- `client_id`: Primary Key
- `first_name`, `last_name`: Client's name
- `current_weight_kg`, `height_cm`: Physical attributes
- `gender`, `age`, `activity_level`
- `body_fat_percentage`, `meal_preference`, `food_allergies`, etc.

## Project Structure
```
.
├── crud.py          # Database operations
├── database.py      # Database setup and session management
├── main.py          # FastAPI application entry point
├── models.py        # Database models
├── routers/        
│   ├── clients.py  # Client-related endpoints
│   ├── get_plan.py # File retrieval endpoints
├── schemas.py       # Pydantic schemas
├── requirements.txt # Dependencies
├── README.md        # Documentation
```

## License
This project is licensed under the MIT License.

## Contact
For support, reach out to [info@six2fit.com](mailto:info@six2fit.com).

