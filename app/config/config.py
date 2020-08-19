import os
from dotenv import load_dotenv
from pathlib import Path
project_folder = Path(__file__).resolve().parent.parent
env_path = Path(project_folder) / ".env"
load_dotenv(dotenv_path=env_path)

DEBUG = os.getenv("DEBUG")
PORT = os.getenv("PORT")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
SECRET = os.getenv("SECRET")
