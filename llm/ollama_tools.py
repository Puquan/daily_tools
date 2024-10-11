import requests
import json

def chat_with_ollama_model(question, model_name, history=None, host='localhost', port=11434):
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
    response = requests.post(f'http://{host}:{port}/api/chat', headers=headers, json=data)
    
    response = response.json()
    
    return response['message']['content']

def chat_with_ollama_model_stream(question, model_name, history=None, host='localhost', port=11434):
    system_message = {"role": "system", "content": "You can ask me any question, and I will try my best to answer it."}
    user_message = {"role": "user", "content": question}
    
    if history is None:
        messages = [system_message, user_message]
    else:
        messages = [system_message] + history + [user_message]
    
    data = {
        "model": model_name,
        "messages": messages,
        "stream": True  
    }

    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.post(f'http://{host}:{port}/api/chat', headers=headers, json=data, stream=True)
    
    if response.status_code == 200:
        # Process the stream of data as it arrives
        for chunk in response.iter_lines():
            if chunk:
                decoded_chunk = chunk.decode('utf-8')
                chunk_data = json.loads(decoded_chunk)  
                
                if 'message' in chunk_data and 'content' in chunk_data['message']:
                    content = chunk_data['message']['content']
                    print(content, end='', flush=True)  
    else:
        print(f"Error: Received status code {response.status_code}")
        
def emb_by_ollama_model(input, model_name, host='localhost', port=11434):
    # Define the data payload
    data = {
        "model": model_name,
        "input": input
    }

    # Set request headers
    headers = {
        'Content-Type': 'application/json',
    }

    # Send POST request
    response = requests.post(f'http://{host}:{port}/api/embed', headers=headers, json=data)
    
    return response.json()["embeddings"]


if __name__ == '__main__':
    question = "你好，你是谁?"
    model_name = "qwen2"
    response = chat_with_ollama_model(question, model_name)
    print(response)
    chat_with_ollama_model_stream("Tell me about the history of AI.", "qwen2")
    input = ["Why is the sky blue?", "Why is the grass green?"]
    result = emb_by_ollama_model(input=input, model_name="bge-m3")
    print(result)
