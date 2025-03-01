import requests
import json

DICTEIT_API_URL = "https://api.dicteit.com/transcribe"
DICTEIT_API_KEY = "your_dicteit_api_key"

# may change to gemini because I think they offer more prompts per time period.
LLM_API_URL = "https://api.openai.com/v1/chat/completions"
LLM_API_KEY = "your_openai_api_key"

def transcribe_audio(audio_file_path):
    """ Sends an audio file to Dicteit API and returns the transcribed text. """
    headers = {"Authorization": f"Bearer {DICTEIT_API_KEY}"}
    files = {"file": open(audio_file_path, "rb")}
    
    response = requests.post(DICTEIT_API_URL, headers=headers, files=files)
    response_data = response.json()
    
    if response.status_code == 200:
        return response_data.get("text", "")
    else:
        raise Exception(f"Dicteit API Error: {response_data}")

def grade_text(text):
    """ Sends transcribed text to an LLM for grading. """
    headers = {
        "Authorization": f"Bearer {LLM_API_KEY}",
        "Content-Type": "application/json"
    }
    
    prompt = f"""
    You are a grading assistant. Evaluate the following response based on clarity, grammar, and content accuracy.
    Provide a grade (A-F) and a brief explanation.

    Response:
    {text}

    Grade and feedback:
    """
    
    payload = {
        "model": "gpt-4",
        "messages": [{"role": "system", "content": prompt}],
        "temperature": 0.3
    }
    
    response = requests.post(LLM_API_URL, headers=headers, json=payload)
    response_data = response.json()
    
    if response.status_code == 200:
        return response_data["choices"][0]["message"]["content"]
    else:
        raise Exception(f"LLM API Error: {response_data}")

if __name__ == "__main__":
    audio_path = "sample_audio.wav"  # Replace with actual audio file path
    try:
        transcribed_text = transcribe_audio(audio_path)
        print("Transcribed Text:", transcribed_text)
        
        grade = grade_text(transcribed_text)
        print("Grading Report:\n", grade)
    except Exception as e:
        print("Error:", e)
