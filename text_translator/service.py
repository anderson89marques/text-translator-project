from decouple import config

from text_translator.client import GoogleTranslateClient

TOKEN = config("TOKEN", default="fake_token")


class TranslatorService:
    def __init__(self) -> None:
        self.client = GoogleTranslateClient.from_credential(TOKEN)

    def translate(self, payload: dict):
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
            return response_payload
