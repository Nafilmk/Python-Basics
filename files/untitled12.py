import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")
with open('data.txt')as f:
    x=f.readlines()
speak.Speak(x)