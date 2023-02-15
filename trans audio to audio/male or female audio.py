import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
   audio_text = r.listen(source)
print(type(audio_text))
print(r.recognize_google(audio_text))
x=str(r.recognize_google(audio_text))
#translate
from translate import Translator
mytext = x
print("choose your lang")
print("1 : french","2 :german","3 : hindi",'4 : spanish','5 : arabic','6 : malayalam','7 : afrikaans')
y=input("choose your lang : ")
if(y=='1'):
    translator= Translator(to_lang="french")
elif(y=='2'):
    translator= Translator(to_lang="german")
elif(y=='3'):
    translator= Translator(to_lang="hindi",)
elif(y=='4'):
    translator= Translator(to_lang="spanish")
elif(y=='5'):
    translator= Translator(to_lang="arabic")
elif(y=='6'):
    translator= Translator(to_lang="malayalam")
elif(y=='7'):
    translator= Translator(to_lang="afrikaans")
translation = translator.translate(x)
#audio
print("0:male","1:female")
z=int(input("choose your sound :"))
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[z].id)
print(translation)
engine.say(translation)
engine.runAndWait()

