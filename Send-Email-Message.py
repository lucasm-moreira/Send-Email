import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime

# Date
today = datetime.now()
day = today.day
month = today.month
year = today.year
hour = today.hour
minute = today.minute
second = today.second

# Email addresses from origin and destiny
from_addr = '<origin address here>'
to_addrs = ['<destiny address here>']
subject = 'Backup - ' + str(day) + '/' + str(month) + '/' + str(year) + ' - ' + str(hour) + ':' + str(minute) + ':' + str(second)

# Message to be sent
message = MIMEMultipart()
message['From'] = from_addr
message['To'] = ','.join(to_addrs)
message['Subject'] = subject

body = 'The daily backup report ' + str(month) + '/' + str(day) + '/' + str(year) + \
       ' at ' + str(hour) + ':' + str(minute) + ':' + str(second) + ' is attached.'
message.attach(MIMEText(body, 'plain'))
file = '<path to your file here>'
attachment = open(file, 'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename = " + file)

message.attach(part)
text = message.as_string()

# Username or email address to login on the server
username = '<origin email address here>'
password = 'password here'

# Conection with Google servers
smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465

# Secure conection using SSL
server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)

# Make login to interact with the external server
server.login(username, password)
server.sendmail(from_addr, to_addrs, text)
server.quit()