import requests

url = "https://gotik-tiktok-api-automation-scrapper-services.p.rapidapi.com/api/solve-captcha"

payload = {
	"iid": "7234567890123456789",
	"did": "7123456789012345678",
	"device_type": "SM-G973N",
	"device_brand": "samsung",
	"country": "US",
	"proxy": "http://user:pass@proxy:port"
}
headers = {
	"x-rapidapi-key": "RAPIDAPI KEY",
	"x-rapidapi-host": "gotik-tiktok-api-automation-scrapper-services.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
