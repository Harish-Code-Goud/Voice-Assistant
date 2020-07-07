import pyttsx3
#import pyaudio
import datetime
import speech_recognition as sr
import wikipedia
#import smtplib
import webbrowser as wb
import os
import psutil
import pyjokes
import pyautogui


engine= pyttsx3.init()
#engine.say("hello harish")
#engine.runAndWait()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#speak("Hello harish")

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    #speak(f'The timeis {time}')
    speak("current time is")
    speak(Time)

#time()

def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month) 
    day=int(datetime.datetime.now().day)
    #speak("The date is")
    speak("today date is")
    speak(day)
    speak(month)
    speak(year)
    
#date()

def wish_me():
    speak("welcome Mr Goud")
    speak("Jarvis at your service sir,how can i help you")

#wish_me()


def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognising..")
        query= r.recognize_google(audio,language='en')
        print(query)

    except Exception as e:
        print(e)
        speak("please repeat again...")
        return "None"

    return query

def screenshot():
    image=pyautogui.screenshot()
    image.save("C:/Users/Harish/Pictures/ss_proj.png")


def cpu_info():
    usage=str(psutil.cpu_percent())
    speak("cpu is at"+usage)

    battery=psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())



#wish_me()

#let's get into the main (function) part

if __name__ == "__main__":

    wish_me()
    
    
    while True:
        i=0                        #used for play next in songs
        query=take_command().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak("searching...")

            query= query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        
        elif 'chrome' in query:
            speak("what should i search")

            chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search1 = take_command().lower()
            speak(f'searching {search1}')
            wb.get(chromepath).open_new_tab(search1+'.com')

        elif 'shutdown' in query:
            os.system("shutdown -1")

        elif 'restart' in query:
            os.system("shutdown /s /t 1")

        elif 'logout' in query:
            os.system("shutdown /r /t -1")

        elif 'play songs' in query:
            songs_dir="C:/Users/Harish/Music"
            song=os.listdir(songs_dir)
            
            os.startfile(os.path.join(songs_dir,song[i]))
        
        elif 'play next' in query:
            i=i+1
            songs_dir="C:/Users/Harish/Music"
            song=os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,song[i]))

        elif 'screenshot' in query:

            screenshot()

        elif 'cpu' in query:
            cpu_info()

        elif 'remember' in query:
            speak("what should i remember")
            data=take_command()
            speak("you said to remember"+data)

            remember=open('remember.txt','w')
            remember.write(data)
            remember.close()

        elif 'any thing to remind':
            rem=open('remember.txt','r')
            speak('you said me to remember'+rem.read())


        elif 'joke' in query:
            jokes()

        elif 'offline' in query:
            speak("going offline sir")
            quit()






