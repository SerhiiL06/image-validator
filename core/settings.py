import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


OPEN_AI_KEY = os.getenv("OPENAI_KEY")
