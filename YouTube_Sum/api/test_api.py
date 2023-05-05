import requests

data = {'prompt': 'Hello, world!'}
response = requests.post('http://127.0.0.1:8000/openai/', json=data)
print(response.json())
