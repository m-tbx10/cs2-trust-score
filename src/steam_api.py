import os
from dotenv import load_dotenv

load_dotenv()

STEAM_API_KEY = os.getenv("STEAM_API_KEY")

if not STEAM_API_KEY:
    raise ValueError("Missing STEAM_API_KEY. Please check your .env file.")

print("Steam API Key successfully loaded into memory!")
