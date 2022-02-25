import yagmail
import os
import time
from datetime import datetime as dt
from dotenv import load_dotenv

load_dotenv()

sender = os.environ['GMAIL']
receiver = os.environ['OUTLOOK']

subject = 'This is an email test sent everyday at 13:15'

contents = """
Here is the content of the email
"""

while True:
    now = dt.now()
    if now.hour == 13 and now.minute == 15:
        yag = yagmail.SMTP(user=sender, password=os.environ['PASSWORD_GMAIL'])
        yag.send(to=receiver, subject=subject, contents=contents)
        print("Email sent! 🚀")
        time.sleep(60)
