import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
   audio_text = r.listen(source)
print(type(audio_text))
print(r.recognize_google(audio_text))
x=str(r.recognize_google(audio_text))
#translate
from translate import Translator
translator= Translator(to_lang="german")
translation = translator.translate(x)
print (translation)
#write
with open("translate.txt",'a')as f:
    f.write(x)
    f.write('  -  ')
    f.write(translation)
    f.write('\n')
    f.close()
