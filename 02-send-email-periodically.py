import yagmail
import os
import time

from dotenv import load_dotenv

load_dotenv()

sender = os.environ['GMAIL']
receiver = os.environ['OUTLOOK']

subject = 'This is a test email send every 5 seconds'

contents = """
Here is the content of the email
"""

while True:
    yag = yagmail.SMTP(user=sender, password=os.environ['PASSWORD_GMAIL'])
    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email sent! 🚀")
    time.sleep(5)
