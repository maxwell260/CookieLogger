# CookieLogger
A script that will steal chrome cookies and sends to you via e-mail

HOW TO USE IT

1. Choose a Google account to use
2. Enable less secure apps from Google account settings
3. Open the script with a text editor
4. Go to line 11, 12, 13 and enter the required data
5. (optional) use pyinstaller (or another py-to-exe compiler) to convert the script into an executable file
6. Run the script (or the exe) on the pc you want to steal cookies from

HOW IT WORKS

1. The script get the username from the pc
2. It use it to enter the AppData folder
3. Gets the Cookies file from "Default" Google Chrome directory
4. Builds an embedded e-mail with that file
5. Sends the e-mail to the given e-mail adress
6. Closes himself


The developer is not responsible for any use made with this script
