import speech_recognition as sr
import pyttsx3
import pyaudio as p
import os
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
        r.pause_threshold=0.5
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
speak("Welcome to voice controlled tic tac toe")
speak("Following is the position matrix as per keypad")
lst=[[" "," "," "],[" "," "," "],[" "," "," "]]
for i in range(3):
    print(lst[i])
print("Positin matrix is as per keypad.....")
print("7 8 9 \n4 5 6\n1 2 3")
speak("Select player one's symbol....")
p1=input_speech()
print("Player One: ",p1)
speak("Select player two's symbol....")
p2=input_speech()
print("Player Two :",p2)
count=0
while(count<9):
    win=0
    if count%2==0:
        speak("Speak Player one's position")
        print("Speak Player one's position......")
        pos=input_speech()
        if pos=="1" or pos=="2" or pos=="3" or pos=="4" or pos=="5" or pos=="6" or pos=="7" or pos=="8" or pos=="9":
            pos=int(pos)
        else:
            print("Invalid Position Recognised")
            speak("Invalid position recognised please speak again from following position matrix")
            print("Speak again from following position matrix")
            print("7 8 9 \n4 5 6\n1 2 3")
            continue
        print("Player One's entry",str(pos))
        if pos==7:
            if lst[0][0]==p1 or lst[0][0]==p2:
                speak("invalid entry re-enter")
                print("Invalid Entry!!!\n Re-enter...")
                continue
            lst[0][0]=p1
            count+=1
        elif pos==8:
            if lst[0][1]==p1 or lst[0][1]==p2:
                speak("invalid entry re-enter")
                print("Invalid Entry!!!\n Re-enter....")
                continue
            lst[0][1]=p1
            count+=1
        elif pos==9:
             if lst[0][2]==p1 or lst[0][2]==p2:
                speak("invalid entry re-enter")
                print("Invalid Entry!!!\n Re-enter....")
                continue
             lst[0][2]=p1
             count+=1
        elif pos==4:
             if lst[1][0]==p1 or lst[1][0]==p2:
                speak("invalid entry re-enter")
                print("Invalid Entry!!!\n Re-enter....")
                continue
             lst[1][0]=p1
             count+=1
        elif pos==5:
             if lst[1][1]==p1 or lst[1][1]==p2:
                speak("invalid entry re-enter")
                print("Invalid Entry!!!\n Re-enter....")
                continue
             lst[1][1]=p1
             count+=1
        elif pos==6:
             if lst[1][2]==p1 or lst[1][2]==p2:
                speak("invalid entry re-enter")
                print("Invalid Entry!!!\n Re-enter....")
                continue
             lst[1][2]=p1
             count+=1
        elif pos==1:
             if lst[2][0]==p1 or lst[2][0]==p2:
                speak("invalid entry re-enter")
                print("Invalid Entry!!!\n Re-enter....")
                continue
             lst[2][0]=p1
             count+=1
        elif pos==2:
             if lst[2][1]==p1 or lst[2][1]==p2:
                speak("invalid entry re-enter")
                print("Invalid Entry!!!\n Re-enter....")
                continue
             lst[2][1]=p1
             count+=1
        elif pos==3:
             if lst[2][2]==p1 or lst[2][2]==p2:
                speak("invalid entry re-enter")
                print("Invalid Entry!!!\n Re-enter....")
                continue
             lst[2][2]=p1
             count+=1
        cp=0
        for i in range(3):  
          for j in range(3):
                if lst[i][j]==p1:
                    cp+=1
          if cp==3:
                speak("player 1 is winner")
                print("Player 1 is Winner!!!!")
                win+=1
                break
          cp=0
        for i in range(3):
            for j in range(3):
                if lst[j][i]==p1:
                    cp+=1
            if cp==3:
                speak("player 1 is winner")
                print("Player 1 is Winner!!!!!")
                win+=1
                break
            cp=0
        cp=0
        for i in range(3):
            if lst[i][i]==p1:
                cp+=1
        if cp==3:
            speak("player 1 is winner")
            print("Player 1 is Winner!!!!!")
            win+=1
            break
        cp=0
        j=2
        for i in range(3):
           if lst[i][j]==p1:
               cp+=1
           j=j-1
        if cp==3:
            speak("Player 1 is winner!!")
            print("Player 1 is Winner!!!!")
            win+=1
        for i in range(3):
            print(lst[i])
    if win>0:
        break
    if count==9:
        speak("Match Draw!!!")
        print("Match Draw!!!!")
    else:
        speak(" Speak Player two's position")
        print("Speak Player Two's Position....")
        pos=input_speech()
        if pos=="1" or pos=="2" or pos=="3" or pos=="4" or pos=="5" or pos=="6" or pos=="7" or pos=="8" or pos=="9":
            pos=int(pos)
        else:
            print("Invalid Position Recognised")
            speak("Invalid position recognised please speak again from following position matrix")
            print("Speak again from following position matrix")
            print("7 8 9 \n4 5 6\n1 2 3")
            continue
        print("Player two's entry",str(pos))
        if pos==7:
             if lst[0][0]==p1 or lst[0][0]==p2:
                speak("invalid entry re-enter")
                print("Invalid Entry!!!\n Re-enter....")
                continue
             lst[0][0]=p2
             count+=1
        elif pos==8:
             if lst[0][1]==p1 or lst[0][1]==p2:
                speak("invalid entry re-enter")
                print("Invalid Entry!!!\n Re-enter....")
                continue
             lst[0][1]=p2
             count+=1
        elif pos==9:
             if lst[0][2]==p1 or lst[0][2]==p2:
                speak("invalid entry re-enter")
                print("Invalid Entry!!!\n Re-enter....")
                continue
             lst[0][2]=p2
             count+=1
        elif pos==4:
             if lst[1][0]==p1 or lst[1][0]==p2:
                speak("invalid entry re-enter")
                print("Invalid Entry!!!\n Re-enter....")
                continue
             lst[1][0]=p2
             count+=1
        elif pos==5:
             if lst[1][1]==p1 or lst[1][1]==p2:
                speak("invalid entry re-enter")
                print("Invalid Entry!!!\n Re-enter....")
                continue
             lst[1][1]=p2
             count+=1
        elif pos==6:
             if lst[1][2]==p1 or lst[1][2]==p2:
                speak("invalid entry re-enter")
                print("Invalid Entry!!!\n Re-enter....")
                continue
             lst[1][2]=p2
             count+=1
        elif pos==1:
             if lst[2][0]==p1 or lst[2][0]==p2:
                speak("invalid entry re-enter")
                print("Invalid Entry!!!\n Re-enter....")
                continue
             lst[2][0]=p2
             count+=1
        elif pos==2:
             if lst[2][1]==p1 or lst[2][1]==p2:
                speak("invalid entry re-enter")
                print("Invalid Entry!!!\n Re-enter....")
                continue
             lst[2][1]=p2
             count+=1
        elif pos==3:
             if lst[2][2]==p1 or lst[2][2]==p2:
                speak("invalid entry re-enter")
                print("Invalid Entry!!!\n Re-enter....")
                continue
             lst[2][2]=p2
             count+=1
        cp=0
        for i in range(3):  
          for j in range(3):
                if lst[i][j]==p2:
                    cp+=1
          if cp==3:
                print("Player 2 is Winner!!!!")
                speak("player two is winner")
                win+=1
                break
          cp=0
        for i in range(3):
            for j in range(3):
                if lst[j][i]==p2:
                    cp+=1
            if cp==3:
                print("Player 2 is Winner!!!!!")
                speak("player two is winner")
                win+=1
                break
            cp=0
        cp=0
        for i in range(3):
            if lst[i][i]==p2:
                cp+=1
        if cp==3:
            print("Player 2 is Winner!!!!!")
            speak("player two is winner")
            win+=1
            break
        cp=0
        j=2
        for i in range(3):
           if lst[i][j]==p2:
               cp+=1
           j=j-1
        if cp==3:
            print("Player 2 is Winner!!!!")
            speak("player two is winner")
            win+=1
        for i in range(3):
            print(lst[i])
    if win>0:
        break
