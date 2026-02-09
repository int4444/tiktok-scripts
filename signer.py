import requests

url = "https://gotik-tiktok-api-automation-scrapper-services.p.rapidapi.com/api/sign"

payload = {
	"url": "https://api.tiktok.com/v1/feed?cursor=0&count=10", ## full URL + params
	"app_id": 1233, ## 1233 = TikTok Global App
	"app_version": "34.8.0", ## tiktok version to use (some tt versions have different request params so choose wisely
	"app_launch_time": 1707072000,
	"device_type": "", ## replace 
	"sdk_version": "", ## replace with sdk ver
	"sdk_version_code": , ## replace with sdk manifest
	"license_id": , ## replace
  ## dyn_version supported
  ## dyn_encrypt not full support
	"device_id": "7197348373476362270",
	"device_token": "", ## put device_token
	"payload": "00000000000000000000000000000000", ## optional
	"cookies": "" ## optional
}
headers = {
	"x-rapidapi-key": "RAPIDAPI KEY", ## REPLACE YOUR RAPIDAPI KEY
	"x-rapidapi-host": "gotik-tiktok-api-automation-scrapper-services.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
