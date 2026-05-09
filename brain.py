import requests
import json


# This enables user to use or interact with AI [AI model name : tinyllama by ollama ]
def ask_ai(prompt):
    try:
        # 🔥 force short & fast response
        prompt = f"Give a very short answer in 2 sentence: {prompt}"

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "tinyllama",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "num_predict": 50,   
                    "temperature": 0.7
                }
            }
        )

        return response.json()["response"]

    except:
        return "Error"
