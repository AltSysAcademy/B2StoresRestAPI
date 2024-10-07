
import os
import requests
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("SQLALCHEMY_DATABASE_URI"))