import smtplib

import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<16:
        speak("good afternoon!")
    else:
        speak("good evening!")

    speak("My name is Ally. How may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("user said: ", query)

    except Exception as e:
        #print(e)
        print("Please say that again...")
        return "none"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('demoo0712@gmail.com','niravdedhiya')
    server.sendmail('dedhiyanirav07@gmail.com',to,content)
    server.close()

if __name__ == '__main__':
    speak("Hello Nirav")
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open github' in query:
            webbrowser.open('github.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            music_dir = 'E:\\Demo'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(str_time)
            print("Sir, the time is: ",str_time)

        elif 'open code' in query:
            path = 'C:\\Users\\nirav\\PycharmProjects\\VoiceAssistant\\ally.py'
            os.startfile(path)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "<receiver's email>"
                sendEmail(to, content)
                speak("email sent")
                print("email sent")
            except Exception as e:
                #print(e)
                speak("unable to send")
                print("unable to send")

