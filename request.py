import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/todos/1"
)

print("status_code =", response.status_code)
print(response.json())