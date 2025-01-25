from fastapi import FastAPI
from .database import engine, Base
from .routers import user

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include the user router
app.include_router(user.router)
