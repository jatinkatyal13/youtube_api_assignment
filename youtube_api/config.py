import os
from dotenv import load_dotenv


load_dotenv()

class Config:
    DEBUG = os.environ.get("DEBUG") in ["True", "true", "1", 1]
    SECRET_KEY = os.environ.get("SECRET_KEY", "abc")
    ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")

    YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY")
    YOUTUBE_KEYWORDS = os.environ.get("YOUTUBE_KEYWORDS", "").split(",")
