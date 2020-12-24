import requests

url = "https://arithmetic-service.herokuapp.com/mul/1/2/3/4/5"

response = requests.get(url)
print(response.text)
