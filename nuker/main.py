import requests

url = "https://franek12345.pythonanywhere.com/create"
for i in range(1000):
    data = {
        "title": f"SPAM {i}",
        "subtitle": "Test spam",
        "text": "Lorem ipsum " * 10
    }
    r = requests.post(url, data=data)
    print(f"{i} -> {r.status_code}")
