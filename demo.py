print("hello dev")
import requests

url = "https://radhachande7-eval-test.apigee.net/v0/hello"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)