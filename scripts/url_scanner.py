import requests

repl = "https://repl.it/"
URL = input("Enter a URL: ")

if "http://" not in URL:
  URL = "http://" + URL
  
response = requests.post(URL)
print("Status Code:", response.status_code)
