# fastapi-social-backend

A backend API built with [FastAPI](https://fastapi.tiangolo.com/) for a social-media-style application.  
Features include users, authentication, post creation/update/delete — modular and ready for extension.

## 📋 Features

- User registration & login (JWT-based)  
- Post CRUD: create, read, update, delete posts   
- Modular architecture: routers for users, posts, auth   
- Configuration via environment variables  
- SQLAlchemy (or similar ORM) + relational database support  
- Pydantic models & schemas for data validation  

## 🧱 Project Structure

.
├── main.py # FastAPI app entry point

├── config.py # Configuration (env variables)

├── database.py # Database connection / session setup

├── models.py # ORM models

├── schemas.py # Pydantic schemas

├── oauth2.py # JWT / token utilities

├── utils.py # Utility functions (hashing, etc)

├── routers/ # Routers: users, posts, auth 

├── requirements.txt # Python dependencies

└── .env # Environment variables (excluded from source)


## 📝 Getting Started

### Prerequisites

- Python 3.11+  
- A relational database (PostgreSQL, MySQL, SQLite)  
- Git & GitHub setup  

### Setup

1. Clone the repository:  
   ```bash
   git clone https://github.com/Anirban1411/fastapi-social-backend.git
   cd fastapi-social-backend
   ```

2. Create and activate a virtual environment:
   
   python3 -m venv venv
   source venv/bin/activate   # On macOS/Linux

3. Install dependencies:
   pip install -r requirements.txt

4.Create a .env file (example values):

DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_USERNAME=your_db_user
DATABASE_PASSWORD=your_db_password
DATABASE_NAME=your_db_name
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

5. Run database migrations or create tables (according to your ORM setup).
6. Start the development server:
   uvicorn main:app --reload
   
## Usage

Use the /users router for signup & CRUD user operations.

Use the /auth router for login & token generation.

Use the /posts router for creating, reading, updating, and deleting posts.

## Author

Anirban Biswas
Currently pursuing BS in CS & Data Analytics at IIT Patna.
GitHub: @Anirban1411
