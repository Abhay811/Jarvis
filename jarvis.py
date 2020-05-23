import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import sys
from googlesearch import search


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 190)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning,")
    elif hour >= 12 and hour < 17:
        speak("Good Afternoon,")
    else:
        speak("Good Evening,")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    # It takes audio as input and return as string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 1800
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='eng-in')
        print(f"User said:{query}\n")

    except Exception as e:
        # print(e)
        speak("Sorry, I am unable to catch....")
        return "None"
    return query


# def sendEmail(to, msg):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('abhaymaurya811@gmail.com', '')
#     server.sendmail('abhaymaurya811@gmail.com', to, msg)
#     server.close()

def find_file(filename, search_path):
    result = []
    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))
        return result


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'who are you' in query:
            speak('I am Jarvis 1 sir')
        elif 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak('According to wikipedia')
            print(results)
            speak(results)
        elif 'open paint' in query:
            paint_path = "C:\\WINDOWS\\system32\\mspaint.exe"
            speak("Opening Paint")
            os.startfile(paint_path)
        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("youtube.com")
        elif 'open google' in query or 'google chrome' in query:
            speak("Opening Google Chrome")
            webbrowser.open("google.com")
        elif 'open stack overflow' in query:
            speak("Opening Stack Overflow")
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query or 'play song' in query:
            speak("Playing music, sir")
            musicdir = 'E:\\Music'
            songs = os.listdir(musicdir)
            os.startfile(os.path.join(musicdir, songs[0]))
        elif 'vs code' in query or 'open visual studio' in query or 'open visual studio code'in query:
            code = "D:\\New folder\\Microsoft VS Code\\Code.exe"
            os.startfile(code)
        elif 'codeforces' in query or 'open codeforces' in query:
            webbrowser.open("codeforces.com")
        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {time}")
        elif 'the date' in query:
            date = datetime.datetime.now()
            speak(f"Sir, the date is {date.day,date.month,date.year}")
        # elif 'open a file' in query:
        #     speak("Sir, What is file name?")
        #     query = takeCommand()
        #     print(query)
        #     print(find_file(query, "E:"))
        elif 'thank you jarvis' in query or 'thank you' in query:
            speak("Welcome, Sir")
            sys.exit(0)
        elif 'get off jarvis' in query:
            speak("Thank you sir")
            sys.exit(0)

            # elif 'send email' in query:
            #     try:
            #         speak("What should I say?")
            #         msg = takeCommand()
            #         to = "abhaymaurya811@gmail.com"
            #         sendEmail(to, msg)
            #         speak("Sir email has been sent")
            #     except Exception as e:
            #         speak("Sorry Sir, I am unable to send...")
