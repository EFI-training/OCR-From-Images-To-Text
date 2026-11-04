import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.environ.get("OPENAI_API_KEY")
BASE_URL = os.environ.get("OPENAI_BASE_URL")

if not API_KEY:
    raise RuntimeError("Set OPENAI_API_KEY in the project .env file.")
if not BASE_URL:
    raise RuntimeError("Set OPENAI_BASE_URL in the project .env file.")

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

__all__ = ["API_KEY", "BASE_URL", "client"]
