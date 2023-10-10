import logging

from decouple import config
from django.core.cache import cache

from text_translator.client import GoogleTranslateClient

TOKEN = config("TOKEN", default="fake_token")

logger = logging.getLogger(__name__)

class TranslatorService:
    def __init__(self) -> None:
        self.client = GoogleTranslateClient.from_credential(TOKEN)

    def translate(self, payload: dict):
        key = f"{payload['language_from']}{payload['language_to']}{payload['text']}"
        if cache.get(key):
            response_payload = payload.copy()
            response_payload["text_translated"] = cache.get(key)
            logger.info("Get text translation from cache.")
            return response_payload
        
        google_payload = {
            "q": payload["text"],
            "source": payload["language_from"],
            "target": payload["language_to"],
            "format": "text",
            "model": "base",
        }
        data = self.client.translate(google_payload)
        if data.get("translations"):
            response_payload = payload.copy()
            first_translation = data.get("translations")[0]
            response_payload["text_translated"] = first_translation["translatedText"]
            cache.set(key, response_payload["text_translated"])
            return response_payload
