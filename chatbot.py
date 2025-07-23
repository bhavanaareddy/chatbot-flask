from dotenv import load_dotenv
import os
import openai
import sqlite3

load_dotenv()  # Loads from .env file
openai.api_key = os.getenv("OPENAI_API_KEY")
