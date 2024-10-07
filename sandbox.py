
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def send_simple_message():
    hello = requests.post(
        "https://api.mailgun.net/v3/sandbox219a369b80a54ba593e1430600b07ce8.mailgun.org/messages",
        auth=("api", "3e5da54e8e130446a534db05b94744d8-5dcb5e36-b01509d2"),
        data={"from": "Python <mailgun@sandbox219a369b80a54ba593e1430600b07ce8.mailgun.org>",
            "to":["altisjessienino18@gmail.com", "altsysacademy@gmail.com"],
            "subject": "Testing from Python",
            "text": "Testing some Mailgun awesomeness!"})
    return hello.json()

print(send_simple_message())