import requests

url = "https://gotik-tiktok-api-automation-scrapper-services.p.rapidapi.com/api/save"

payload = {
	"videoID": "7234567890123456789",
	"sessionid": "your_tiktok_session_id"
}
headers = {
	"x-rapidapi-key": "RAPIDAPI KEY",
	"x-rapidapi-host": "gotik-tiktok-api-automation-scrapper-services.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
