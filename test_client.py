import requests
import time

URL = "http://127.0.0.1:8000/llm-protected"

for i in range(6):
    try:
        res = requests.get(URL)
        print(i, res.json())
    except Exception as e:
        print("Error:", e)

    time.sleep(1)
