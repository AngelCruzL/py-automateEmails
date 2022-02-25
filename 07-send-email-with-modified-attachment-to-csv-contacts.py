import yagmail
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

sender = os.environ['GMAIL']
yag = yagmail.SMTP(user=sender, password=os.environ['PASSWORD_GMAIL'])

df = pd.read_csv('contacts.csv')


def generate_filename(filename, content):
    with open(filename, 'w') as file:
        file.write(str(content))


for index, row in df.iterrows():
    name = row['name']
    filename = f'{name}.txt'
    amount = row['amount']
    receiver_email = row['email']

    generate_filename(filename, amount)

    subject = 'This is an email test with an modified attachment!'
    contents = [f"""
Hey {name}, you have to pay {amount}.
Bill is attached!.""",
                filename]

    yag.send(to=row['email'], subject=subject, contents=contents)
    print("Email sent! 🚀")
