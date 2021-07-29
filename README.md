# CookieLogger
A script that will extract chrome cookies and sends to you via e-mail

CookieLogger is a script I made using Python to test the online accounts security.
Noedays, many websites reccomend to use strong passwords and other security tricks, but is not useful at all if the login is not required EVERY TIME you open the website. Infact, a lot of websites are able to know which device is trying to acces from, allowing you to bypass the login by saving a cookie file into your PC.
And what if that file was in another device?

IMPORTANT
1. The given e-mail must be a Google based e-mail (example@gmail.com)
2. Both PCs must have an Internet connection and be able to reach Gmail servers

HOW TO USE IT

1. Choose a Google account to use
2. Enable less secure apps from Google account settings
3. Open the script with a text editor
4. Go to line 12, 13, 14 and enter the required data
5. (optional) use pyinstaller (or another py-to-exe compiler) to convert the script into an executable file
6. Run the script (or the exe) on the PC you want to extract cookies from

HOW IT WORKS

1. The script get the username from the PC
2. It use it to enter the AppData folder
3. Gets the Cookies file from "Default" Google Chrome directory
4. Builds an embedded e-mail with that file
5. Sends the e-mail to the given e-mail adress
6. Closes himself


The developer is not responsible for any use made with this script
