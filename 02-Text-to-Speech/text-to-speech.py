from gtts import gTTS
import os
text = input("Enter text to speak: ")
print("Processing...")
tts = gTTS(text=text, lang='en')
tts.save("output.mp3")
print("Playing...")
os.system("start output.mp3")