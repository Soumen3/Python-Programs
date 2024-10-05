import pywhatkit as kit

# Replace 'phone
# _number' with the recipient's phone number including the country code (e.g., +1234567890)
phone_number = '+918207286313'

# Replace 'message' with the message you want to send
message = 'Hello, this is a test message sent using Python!'

# Send the message
kit.sendwhatmsg(phone_number, message, 1, 2, 1)