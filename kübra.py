from gtts import gTTS
import os

mytext = "deneme ses";
audio = gTTS(text=mytext, lang="tr", slow=False)

audio.save("demo.mp3")
os.system("start demo.mp3")