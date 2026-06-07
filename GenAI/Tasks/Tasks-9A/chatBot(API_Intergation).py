import requests
API_KEY = 'AIzaSyCjDfVz2Dc1I3nKYAreyxT2q57ggHdH9a0'
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

while(True):
    inp = input("Enter your query: ")

    headers = {
        "x-goog-api-key": API_KEY,
        'Content-Type': 'application/json'
    }
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": inp}
                ]
            }
        ]
    }

    if inp == "stop":
        break
    else:
        response = requests.post(url, headers=headers, json=payload)

        print("Status", response.status_code)

        data = response.json()
        print(data)

        if "candidates" in data:
            print(data["candidates"][0]["content"]["parts"][0]["text"])
        else:
            print("Error", data)




