import os
from dotenv import load_dotenv

load_dotenv()

TRAFIKVERKET_API_KEY = os.getenv('TRAFIKVERKET_API_KEY')
