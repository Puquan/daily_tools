import requests
import os
import json

def chat_with_ollama_model(question, model_name, history=None, port=11434):
    
    # Define the data payload
    system_message = {"role": "system", "content": "You can ask me any question, and I will try my best to answer it."}
    user_message = {"role": "user", "content": question}
    
    if history is None:
        messages = [system_message, user_message]
    else:
        messages = [system_message] + history + [user_message]
    
    data = {
        "model": model_name,
        "messages": messages,
        "stream": False
    }

    # Set request headers
    headers = {
        'Content-Type': 'application/json',
    }

    # Send POST request
    response = requests.post(f'http://localhost:{port}/api/chat', headers=headers, json=data)
    
    response = response.json()
    
    return response['message']['content']

if __name__ == '__main__':
    question = "你好，你是谁?"
    model_name = "llama3.1:8b"
    response = chat_with_ollama_model(question, model_name)
    print(response)