# import json
# from urllib.request import urlopen

# url = 'http://ipinfo.io/json'
# response = urlopen(url)  # get the response from url
# data = json.load(response)

# print(data)
# arr = data["loc"].split(',')
# print(arr)
# print(f"longitude:{arr[0]}")
# print(f"latitute:{arr[1]}")
import requests

def get_current_location():
    try:
        # Make a GET request to the ip-api.com API
        response = requests.get('http://ip-api.com/json')

        if response.status_code == 200:
            data = response.json()
            latitude = data['lat']
            longitude = data['lon']
            print(data)
            print (data['city'])
            return float(latitude), float(longitude)
        else:
            return None

    except Exception as e:
        return None


current_location = get_current_location()
if current_location:
    latitude, longitude = current_location
    print(f"Current Location (Latitude, Longitude): {latitude}, {longitude}")
else:
    print("Location information not available.")
