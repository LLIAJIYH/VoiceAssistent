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


def say(what):
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(what)


say("What do you want me to say?")
i = input("What do you want me to say? ")
say(i)
