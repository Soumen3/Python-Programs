import requests

# Your friend's mobile number
mobile_number = ""

# The message you want to send
message = "This is a popup message!"

# The URL of the API to send the popup message
api_url = "https://api.example.com/send-popup-message"

# Set the headers for the API request
headers = {
    "Content-Type": "application/json"
}

# Set the body of the API request
body = {
    "mobile_number": mobile_number,
    "message": message
}

# Make the API request
response = requests.post(api_url, headers=headers, json=body)

# Check if the API request was successful
if response.status_code == 200:
    print("Popup message sent successfully!")
else:
    print("Error sending popup message:", response.status_code)


import http.client, urllib
conn = http.client.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.parse.urlencode({
    "token": "APP_TOKEN",
    "user": "USER_KEY",
    "message": "hello world",
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()