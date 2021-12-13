import yagmail
import os
from dotenv import load_dotenv

load_dotenv()

sender = 'langelcruzlara@gmail.com'
receiver = 'langelcruzlara@hotmail.com'

subject = 'This is an email test with an attachment'

contents = ["""
Here is the content of the email
""", 'file.txt']

yag = yagmail.SMTP(user=sender, password=os.environ['PASSWORD'])
yag.send(to=receiver, subject=subject, contents=contents)
print("Email sent! 🚀")
