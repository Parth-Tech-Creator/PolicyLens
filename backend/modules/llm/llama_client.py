import requests
import json


class LlamaClient:
    def __init__(self, model_name: str = "llama3.1:8b", base_url: str = "http://localhost:11434/api/generate"):
        self.model_name = model_name
        self.base_url = base_url

    def ask(self, prompt: str) -> str:
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False,
        }
        try:
            response = requests.post(self.base_url, json=payload)
            data = response.json()
            return data.get("response", "No response from Llama.")
        except Exception as e:
            return f"Error connecting to Ollama: {e}"

