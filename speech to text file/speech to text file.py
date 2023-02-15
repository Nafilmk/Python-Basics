import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
   audio_text = r.listen(source)
print(type(audio_text))
print(r.recognize_google(audio_text))
x=str(r.recognize_google(audio_text))
with open("speek.txt",'a')as f:
    f.write('\n')
    f.write(x)
    f.close()
    