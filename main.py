# Speech
# Voice Assistant using python

import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import pyjokes
import os
import time

# Speech to Text
while True:
    def sptext():
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening..")
            recognizer.adjust_for_ambient_noise(source)
            # Lets create anaother variable listen our audio
            audio = recognizer.listen(source)
            # Now we will the read the data.
            try:
                print("Recognizing....")
                data = recognizer.recognize_google(audio)
                return data
            except sr.UnknownValueError:
                print("Not Understanding")


    # Text to Speech
    def speechtx(x):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        rate = engine.getProperty('rate')
        engine.setProperty('rate', 150)
        engine.say(x)
        engine.runAndWait()


    if __name__ == "__main__":
        if "hey peter" in sptext().lower():
            while True:
                data1 = sptext().lower()
                if "your name" in data1:
                    name = "my name is peter"
                    speechtx(name)

                elif "old are you" in data1:
                    age = "I am two years old"
                    speechtx(age)

                # Now time asking
                elif "time" in data1:
                    time = datetime.datetime.now().strftime("%I%M%p")
                    speechtx(time)

                # Web Browser
                elif 'open youtube' in data1:
                    webbrowser.open("https://www.youtube.com/")

                elif "open facebook" in data1:
                    webbrowser.open("https://www.facebook.com/")

                # using PyJokes
                elif "joke" in data1:
                    joke_1 = pyjokes.get_joke(language='en')  # , category = "neutral")
                    print(joke_1)
                    speechtx(joke_1)

                # you can add many things here to increase say I want to play music

                # when you want to work in your system files you call os
                elif "play song" in data1:
                    address = "song location address"
                    listsong = os.listdir(address)
                    print(listsong)
                    os.startfile(os.path.join(address, listsong[0]))

                # close the program
                elif "exit" in data1:
                    speechtx("thank-you")
                    print("thank-you")
                    break

                # For time delay
                time.sleep(5)
    else:
        print("Thank-you")

