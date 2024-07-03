import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
SECRET = os.getenv('SECRET')
PASSPHRASE = os.getenv('PASSPHRASE')
