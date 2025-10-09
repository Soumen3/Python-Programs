import requests
import getpass
import socket
from datetime import datetime
from pytz import timezone

# Replace with your Discord Webhook URL
WEBHOOK_URL = "https://discord.com/api/webhooks/1425708252762603582/qarVZKSVNLQSnR8OO5EEWfdFc6Ky5GZDpXfWShgSSvSY4qUznscoR1bMA8IvW6_c5ANb"

def send_discord_message():
    user = getpass.getuser()
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    india_tz = timezone('Asia/Kolkata')
    time = datetime.now(india_tz).strftime("%Y-%m-%d %H:%M:%S")

    message = f"💻 **Login Alert**\n👤 User: `{user}`\n🕒 Time: {time}\n💡 Hostname: `{hostname}`\n🌐 IP: `{ip}`"

    payload = {"content": message}
    requests.post(WEBHOOK_URL, json=payload)

if __name__ == "__main__":
    send_discord_message()
