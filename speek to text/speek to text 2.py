import speech_recognition as sr
i=0
while(i>=0):
    r = sr.Recognizer()
    with sr.Microphone() as source2:
        audio_text = r.listen(source2)
        try:
            text = r.recognize_google(audio_text)
            #print('Converting audio transcripts into text ...')
            print(text)
        except:
             print('Sorry.. run again...')
             