import requests

url = "https://yt-api.p.rapidapi.com/search"

querystring = {"query":"cat"}

headers = {
	"x-rapidapi-key": "0ee66910fbmsh0784953505f49b5p157e20jsnf2bb9a40e224",
	"x-rapidapi-host": "yt-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())