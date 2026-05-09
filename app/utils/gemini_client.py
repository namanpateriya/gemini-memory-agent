import google.generativeai as genai

from app.config import GEMINI_API_KEY, MODEL_NAME
from app.utils.logger import get_logger

logger = get_logger(__name__)


class GeminiClient:

    def __init__(self):
        if not GEMINI_API_KEY:
            raise ValueError("Missing GEMINI_API_KEY")

        genai.configure(api_key=GEMINI_API_KEY)

        self.model = genai.GenerativeModel(MODEL_NAME)

    def generate(self, prompt: str):
        try:
            response = self.model.generate_content(prompt)

            if hasattr(response, "text") and response.text:
                return response.text

            return "error: empty response"

        except Exception as e:
            logger.error(f"Gemini generation failed: {e}")
            return f"error: {str(e)}"
