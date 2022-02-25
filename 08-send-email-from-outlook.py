from email import message
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

sender = os.environ['OUTLOOK']
receiver = os.environ['GMAIL']
password = os.environ['PASSWORD_OUTLOOK']

message = """\
Subject: Hello from a Python script

This is Luis
Just wanted to say hi!
"""

# Start the server to send the email
server = smtplib.SMTP('smtp.office365.com', 587)
# Starts on TLS encryption protocol
server.starttls()

server.login(sender, password)
server.sendmail(sender, receiver, message)
server.quit()
