import pyttsx3

bot = pyttsx3.init()
text = input("Say something: ")

bot.say(text)
bot.runAndWait()