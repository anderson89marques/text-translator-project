import os
from urllib.parse import urljoin

import requests

BASE_URL = os.environ.get("EXTERNAL_API", default="https://translation.googleapis.com/language/translate/v2/")


class GoogleTranslateSession(requests.Session):
    def __init__(self, token=None) -> None:
        super().__init__()
        self.base_url = BASE_URL
        self.token = token
        self.headers.update({
            "Content-Type": "application/json",
            "X-goog-api-key": f"{self.token}"
        })
    
    def request(self, method, url, *args, **kwargs):
        path = urljoin(self.base_url, url)
        return super().request(method, path, *args, **kwargs)


class GoogleTranslateClient:
    def __init__(self, session) -> None:
        self.session = session

    @classmethod
    def from_credential(cls, token):
        session = GoogleTranslateSession(token)
        return cls(session)
    
    def translate(self, payload: dict):
        """
        payload = 
        { 
            "q":"loren ipsum...."
            "source":"en",
            "target":"pt",
            "format": "text",
            "model": "base"
        }
        """
        response = self.session.post(
            "",
            json=payload
        )
        return response.json()
        

    def languages(self):
        response = self.session.get("languages")
        data = response.json()
        return data
