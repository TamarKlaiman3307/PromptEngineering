import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

project_dir = Path(__file__).resolve().parents[2]
load_dotenv(project_dir / ".env")

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

for model in client.models.list():
    print(model.name)