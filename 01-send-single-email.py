import yagmail
import os
from dotenv import load_dotenv

load_dotenv()

sender = os.environ['GMAIL']
receiver = os.environ['OUTLOOK']

subject = 'Hello form a Python script 🚀'

contents = """
Here is the content of the email

And here is the second line
"""

yag = yagmail.SMTP(user=sender, password=os.environ['PASSWORD_GMAIL'])
yag.send(to=receiver, subject=subject, contents=contents)
print("Email sent! 🚀")
