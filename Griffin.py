import tkinter as tk
from tkinter.ttk import*
import requests
from speaker import *
import datetime
import os
import wikipedia
import webbrowser
import random
import weather
from translate import Translator

HEIGHT = 512
WIDTH = 435



def wish_user():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    elif hour>=18 and hour<24:
        speak(" Good Evening! ")
    else:
        speak("Good Night!")
    speak(" welcome! ")

def tr():
    print("Enter the language in which you want to convert your text:")
    speak("Enter the language in which you want to convert your text:")
    lang=input_speech()
    print("Do you want to enter data or speak data or do you want to exit ? ")
    speak("Do you want to enter data or speak data or do you want to exit ? ")
    flag=input_speech()
    t=Translator(to_lang=lang)
    if flag=="enter data":
        dat=input("Enter data.....")
        translation=t.translate(dat)
        speak(translation)
    elif flag=="exit":
        speak("bye")
    elif flag=="speak data":
        speak("speak the data to be translated")
        data=''
        speak("Speak Sir")
        data=input_speech()
        translation=t.translate(data)
        speak(translation)
    else:
        speak("please enter the right choise")
        tr()

def play():
    speak("Let us play Tic tAC toe")
    os.startfile("tictac.py")

def Griffin():
    query=input_speech()
    query=query.lower()
    if 'wikipedia' in query:
        speak("Finding information in wikipedia")
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=2)
        speak("with refrence to wikipedia")
        speak(results)
    elif 'open youtube' in query:
        speak("opening youtube")
        webbrowser.open("youtube.com")
    elif "exit" in query:
        exit()
    elif 'play game' in query:
        speak("Let us play Tic tAC toe")
        os.startfile(r"C:\Users\admin\AppData\Local\Programs\Python\Python37-32\tictac.py")
    elif 'open google' in query:
        speak("opening google")
        webbrowser.open("google.com")
    elif "translate" in query:
        translate()
    elif query.find('open')!=-1:
        q=query.replace("open","")
        q=q.strip()
        print(q)
        speak("opening"+q+".com")
        webbrowser.open(q+".com")
    elif 'bye' in query or 'end' in query:
        exit()
    else :
        speak("you said"+query)
def know_me():
    speak("i am marion do you want to know about me??")
    query=input_speech()
    if query=="yes":
        speak("i was created by a team of students, and i was named after the protagonist of the famous novel the invisible man and i can perform all basic operations through your voice commands i am always happy to help")
    else:
        speak("ok you can know about me later")
if __name__=="__main__":
    root = tk.Tk()
    root.title("Assistant")
    root.resizable(0,0)

    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    background_image = tk.PhotoImage(file='pic.png')
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)
    intro=tk.PhotoImage(file="intro.png")
    button1 = tk.Button(root, fg="black", bg="white", borderwidth=0, font=80,image= intro, command=lambda: know_me())
    button1.place(relx=0.42, rely=0.15, relheight=0.15, relwidth=0.2)
    mic=tk.PhotoImage(file="mic.png")
    button2 = tk.Button(root, bg="white", fg="black", borderwidth=0, font=80, image= mic, command=lambda: atmaram())
    button2.place(relx=0.166, rely=0.42, relheight=0.18, relwidth=0.22)
    weather1=tk.PhotoImage(file="weather.png")
    button3 = tk.Button(root, bg="white", fg="black", borderwidth=0, image=weather1, font=80, command=lambda: weather.weather())
    button3.place(relx=0.39, rely=0.695, relheight=0.18, relwidth=0.25)
    trans=tk.PhotoImage(file="trans.png")
    button4 = tk.Button(root, bg="white", fg="black", borderwidth=0, image=trans, font=80, command=lambda: tr())
    button4.place(relx=0.08, rely=0.75, relheight=0.15, relwidth=0.15)
    tictac=tk.PhotoImage(file="tictac.png")
    button5 = tk.Button(root, bg="white", fg="black", borderwidth=0, image=tictac, font=80, command=lambda: play())
    button5.place(relx=0.763, rely=0.8, relheight=0.15, relwidth=0.15)
    rem=tk.PhotoImage(file="rem.png")
    button6 = tk.Button(root, bg="white", fg="black", borderwidth=0, image=rem, font=80, command=lambda: exit())
    button6.place(relx=0.07, rely=0.04, relheight=0.13, relwidth=0.15)
    wish_user()
