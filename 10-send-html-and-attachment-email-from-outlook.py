import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
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
<p>I'm attaching you the <a href="https://www.python.org/" target="_blank">python's</a> logo</p>
</body>
</html>
"""

# Set the content of the email as html
mimetext = MIMEText(body, 'html')
message.attach(mimetext)

attachment_path = './python-logo.jpg'
# Reads the file and returns a file object
attachment_file = open(attachment_path, 'rb')
payload = MIMEBase('application', 'octate-stream')
# After reading the file object, the data is stored in the payload variable (in binary mode)
payload.set_payload((attachment_file).read())
# Converts the data into base64 format
encoders.encode_base64(payload)
payload.add_header('Content-Disposition', 'attachment',
                   filename=attachment_path)
message.attach(payload)

# Start the server to send the email
server = smtplib.SMTP('smtp.office365.com', 587)
# Starts on TLS encryption protocol
server.starttls()

server.login(sender, password)
message_text = message.as_string()
server.sendmail(sender, receiver, message_text)
server.quit()
