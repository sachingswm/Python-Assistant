import speech_recognition as sr
import pyttsx3
import pyaudio as p
engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',150)
def speak(q):
    engine.say(q)
    engine.runAndWait()
def input_speech():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognising.....")
        query=r.recognize_google(audio,language='en-in')
        print("you said......"+query)
    except Exception as e:
        print(e)
        print("Sorry Say tha Again...")
        return input_speech()
    return query
