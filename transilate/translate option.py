import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
   audio_text = r.listen(source)
print(type(audio_text))
print(r.recognize_google(audio_text))
x=str(r.recognize_google(audio_text))
#translate
from translate import Translator
print("choose your lang")
print("1 : eng","2 :german","3 : albanian",'4 : spanish','5 : arabic','6 : malayalam','7 : afrikaans')
y=input("choose your lang : ")
if(y=='1'):
    translator= Translator(to_lang="english")
elif(y=='2'):
    translator= Translator(to_lang="german")
elif(y=='3'):
    translator= Translator(to_lang="albanian")
elif(y=='4'):
    translator= Translator(to_lang="spanish")
elif(y=='5'):
    translator= Translator(to_lang="arabic")
elif(y=='6'):
    translator= Translator(to_lang="malayalam")
elif(y=='7'):
    translator= Translator(to_lang="afrikaans")
translation = translator.translate(x)
print (translation)
#write
with open("transoption.txt",'a')as f:
    f.write(x)
    f.write('  -  ')
    f.write(translation)
    f.write('\n')
    f.close()