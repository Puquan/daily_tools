import requests
import os
import json

API_KEY = os.getenv("DEEPSEEK_API_KEY")

def chat_with_deepseek_model(question, model_name, history=None):
    
    # Define the data payload
    system_message = {"role": "system", "content": "You are an AI programming assistant, utilizing the DeepSeek Coder model, developed by DeepSeek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer."}
    user_message = {"role": "user", "content": question}
    
    if history is None:
        messages = [system_message, user_message]
    else:
        messages = [system_message] + history + [user_message]
    
    data = {
        "model": model_name,
        "messages": messages,
    }

    # Set request headers
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}',
    }

    # Send POST request
    response = requests.post(f'https://api.deepseek.com/chat/completions', headers=headers, json=data)

    # Convert response content to JSON format and read
    response_json = json.loads(response.text)
    
    # Return the completion content
    return response_json['choices'][0]['message']['content']

if __name__ == '__main__':
    question = "你好，你是谁?"
    model = 'deepseek-coder'
    response = chat_with_deepseek_model(question, model)
    print(response)
        