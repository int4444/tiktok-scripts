import requests

url = "https://gotik-tiktok-api-automation-scrapper-services.p.rapidapi.com/api/decrypt"

payload = { "data": "a3f8b9c2d5e1f4a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4" }
headers = {
	"x-rapidapi-key": "RAPIDAPI KEY",
	"x-rapidapi-host": "gotik-tiktok-api-automation-scrapper-services.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
