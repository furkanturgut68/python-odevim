import speech_recognition as sr

r = sr.Recognizer()

# pip install SpeechRecognition

file = sr.AudioFile('demo.mp3')

with file as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)
    result = r.recognize_google(audio, language="eng")
print(result)