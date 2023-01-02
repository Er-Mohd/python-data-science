import requests

url = 'http://www.google.com/search?q=python'
responce = requests.get(url)
if responce.status_code ==200:
    print("Success!")
    print(responce.text)
else:
    print('An error has accurred.')