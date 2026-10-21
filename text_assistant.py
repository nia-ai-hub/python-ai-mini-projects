import subprocess
import pyttsx3

bot = pyttsx3.init()
command = input("Command: ").lower()
text = command

apps = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe"
}

if command in apps:
    subprocess.Popen(apps[command]) 
    bot.say(text + "it's open right now")
    bot.runAndWait()
else:
    print("Unknown command") 
    bot.say(text + "it's unknown command")
    bot.runAndWait()