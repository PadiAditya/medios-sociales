import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "qwerty@123")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///medios-sociales.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "qwerty@123")