import speech_recognition as sr
print(sr.__version__)
r = sr.Recognizer()
with sr.Microphone() as source:
   audio_text = r.record(source)

print(type(audio_text))
print(r.recognize_google(audio_text))