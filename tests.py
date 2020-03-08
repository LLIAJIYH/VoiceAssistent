import pyttsx3
import speech_recognition as sr
import os
from fuzzywuzzy import fuzz
import datetime
import win32com.client as wincl
startTime = 0
speak_engine = pyttsx3.init()
voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[2].id)
voice = "str"
speak = wincl.Dispatch("SAPI.SpVoice")
i = input("Что мне произнести? ")
speak.Speak("Что мне произнести?")
speak.Speak(i)

