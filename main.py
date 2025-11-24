from fastapi import FastAPI
from database import engine, get_db, SessionLocal
import models
from routers import posts, users, auth;

# --- Create DB Tables (SQLAlchemy - run once or use Alembic later) ---
models.Base.metadata.create_all(bind=engine)
 # This line creates tables

# ... (FastAPI app instance and other imports) ...

app = FastAPI()

#for the posts segment in the router folder
app.include_router(posts.router)

#for the users segment in the router folder
app.include_router(users.router)

#for the auth segment in the router folder
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Hello World"}
