import requests

url = "https://gotik-tiktok-api-automation-scrapper-services.p.rapidapi.com/api/encrypt"

payload = { "data": "ENCRYPTED" }
headers = {
	"x-rapidapi-key": "RAPIDAPI KEY HERE",
	"x-rapidapi-host": "gotik-tiktok-api-automation-scrapper-services.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
