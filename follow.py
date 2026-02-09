import requests

url = "https://gotik-tiktok-api-automation-scrapper-services.p.rapidapi.com/api/follow"

payload = {
	"username": "usernametofollow",
	"sessionid": "your_tiktok_session_id"
}
headers = {
	"x-rapidapi-key": "YOUR RAPIDAPI KEY",
	"x-rapidapi-host": "gotik-tiktok-api-automation-scrapper-services.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
