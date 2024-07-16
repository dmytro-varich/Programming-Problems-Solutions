import requests

url = "http://127.0.0.1:3000/api/courses/3"
data = {"name": "C#", "videos": 1}
headers = {"Content-Type": "application/json"}

# res = requests.get(url)
# res = requests.delete(url)
# res = requests.post(url, json=data, headers=headers)
res = requests.put(url, json=data, headers=headers)
print(res.json())
