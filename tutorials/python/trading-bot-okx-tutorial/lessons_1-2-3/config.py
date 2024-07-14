import os
from dotenv import load_dotenv

load_dotenv()

NAME = os.getenv('NAME')
API_KEY = os.getenv('API_KEY')
SECRET = os.getenv('SECRET')
PASSPHRASE = os.getenv('PASSPHRASE')
IS_DEMO = os.getenv('IS_DEMO')

SYMBOL = os.getenv('SYMBOL')
TIMEFRAME = os.getenv('TIMEFRAME')
QTY = os.getenv('QTY')
TIMEOUT = os.getenv('TIMEOUT')

SMA_FAST = os.getenv('SMA_FAST')
SMA_SLOW = os.getenv('SMA_SLOW')




