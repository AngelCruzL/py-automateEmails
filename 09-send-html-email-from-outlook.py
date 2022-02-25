import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

sender = os.environ['OUTLOOK']
receiver = os.environ['GMAIL']
password = os.environ['PASSWORD_OUTLOOK']

message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = 'Hello from a multipart email'

body = """
<html>
<body>
<h2>Hello From a python script 🐍</h2>
<p>This is a multipart email</p>
</body>
</html>
"""

mimetext = MIMEText(body, 'html')
message.attach(mimetext)

# Start the server to send the email
server = smtplib.SMTP('smtp.office365.com', 587)
# Starts on TLS encryption protocol
server.starttls()

server.login(sender, password)
message_text = message.as_string()
server.sendmail(sender, receiver, message_text)
server.quit()
