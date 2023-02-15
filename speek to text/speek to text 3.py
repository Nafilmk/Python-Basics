import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
   audio_text = r.listen(source)
print(type(audio_text))
print(r.recognize_google(audio_text))