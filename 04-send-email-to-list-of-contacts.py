import yagmail
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

sender = 'langelcruzlara@gmail.com'

subject = 'This is a test 🥴'


yag = yagmail.SMTP(user=sender, password=os.environ['PASSWORD'])

df = pd.read_csv('contacts.csv')
print(df)

for index, row in df.iterrows():
    contents = f"""
Hi {row['name']} is the coolest email ever!
"""

    yag.send(to=row['email'], subject=subject, contents=contents)
    print("Email sent! 🚀")
