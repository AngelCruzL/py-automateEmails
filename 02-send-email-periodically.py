import yagmail
import os
import time

from dotenv import load_dotenv

load_dotenv()

sender = 'langelcruzlara@gmail.com'
receiver = 'langelcruzlara@hotmail.com'

subject = 'This is a test'

contents = """
Here is the content of the email
"""

while True:
    yag = yagmail.SMTP(user=sender, password=os.environ['PASSWORD'])
    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email sent! 🚀")
    time.sleep(5)
