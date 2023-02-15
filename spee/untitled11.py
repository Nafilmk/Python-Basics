import win32com.client as wincom
import time
speak = wincom.Dispatch("SAPI.SpVoice")
text = "hello world"
speak.Speak(text)
time.sleep(1)
text = "python text-to-speech test"
speak.Speak(text)