import yagmail
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

sender = os.environ['GMAIL']
subject = 'This is an email test with an attachment'
yag = yagmail.SMTP(user=sender, password=os.environ['PASSWORD_GMAIL'])

df = pd.read_csv('contacts.csv')

for index, row in df.iterrows():
    contents = [f"""
Hey {row['name']}, you have to pay {row['amount']}.
bill is attached.
""", row['filepath']]

    yag.send(to=row['email'], subject=subject, contents=contents)
    print("Email sent! 🚀")
