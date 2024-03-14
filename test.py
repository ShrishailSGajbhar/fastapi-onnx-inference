import requests

payload = {"phrase":"The movie was so good!"}

response = requests.post("http://0.0.0.0:8000/predict", json=payload)

if response.status_code==200:
    prediction = response.json()
    if prediction['sentiment']=="positive":
        print("The phrase is classified as positive.")
    else:
        print("The phrase is classified as negative.")
else:
    print("Failed to get prediction. Please try again.")