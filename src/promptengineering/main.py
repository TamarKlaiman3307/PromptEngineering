from google.genai import types
import gradio as gr
import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# טעינת מפתח ה-API מקובץ .env
project_dir = Path(__file__).resolve().parents[2]
load_dotenv(project_dir / ".env")

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY"),
    http_options=types.HttpOptions(timeout=20000)
)

# הפרומפט  שלנו
SYSTEM_PROMPT = (project_dir / "prompts" / "prompt_v1.txt").read_text(encoding="utf-8")

def convert_to_command(text):
    try:
        print("1. Sending request to Gemini...", flush=True)

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=SYSTEM_PROMPT + "\nUser request: " + text
        )

        print("2. Response received!", flush=True)
        return response.text or "ERROR"

    except Exception as e:
        print("Gemini error:", str(e), flush=True)
        return "API ERROR - check terminal"

app = gr.Interface(
    fn=convert_to_command,
    inputs=gr.Textbox(label="הכניסי הוראה בעברית"),
    outputs=gr.Textbox(label="פקודת CLI"),
    title="Natural Language to CLI",
    description="המרת הוראות בשפה טבעית לפקודות Windows"
)

app.launch()
