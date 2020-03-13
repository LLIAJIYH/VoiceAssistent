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


# TODO add self-bot as assistant


def say(what):
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(what)


def start():
    say("Что мне произнести?")
    i = input("Что мне произнести? ")
    say(i)
