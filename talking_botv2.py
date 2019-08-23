import sys
import random
import datetime
import webbrowser
import pyttsx3
import wikipedia
import pyowm
from colorama import init, Fore, Style, Back
from googlesearch import search
from pygame import mixer
import speech_recognition as sr
from speech_recognition.__main__ import r, audio

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)
rate = engine.getProperty('rate')

engine.setProperty('rate', rate - 90)

greetings = ['hey there', 'hello', 'hi', 'Hai', 'hey!', 'hey']
question = ['How are you?', 'How are you doing?']
responses = ['Okay', "I'm fine"]
var1 = ['who made you', 'who created you']
var2 = ['I_was_created_by_Atulya Singh.', 'Atulya', 'Some_guy_whom_i_never_got_to_know.']
var3 = ['what time is it', 'what is the time', 'time']
var4 = ['who are you', 'what is you name']
cmd1 = ['open browser', 'open google']
search = ['search internet', 'Search internet', 'Search Internet', 'search Internet']
cmd2 = ['play music', 'play songs', 'play a song', 'play some music', 'play a song']
cmd3 = ['tell a joke', 'tell me a joke', 'say something funny', 'tell something funny']
jokes = ['Can a kangaroo jump higher than a house? Of course, a house doesn’t jump at all.', 'My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.', 'Doctor: Im sorry but you suffer from a terminal illness and have only 10 to live Patient: What do you mean, 10? 10 what? Months? Weeks?!"Doctor: Nine.']
cmd4 = ['open youtube', 'i want to watch a video', 'open YouTube']
cmd5 = ['tell me the weather', 'weather', 'what about the weather', 'Weather']
cmd6 = ['exit', 'close', 'goodbye', 'nothing']
cmd7 = ['what is your color', 'what is your colour', 'your color', 'your color?']
colrep = ['I don\'t know, you tell me', 'Actually, I don\'t have eyes, maybe you could help me', 'I just changed it for you']
cmd8 = ['what is you favourite colour', 'what is your favourite color']
cmd9 = ['thank you']
cmd10 = ['Book Train Tickets', 'book Train tickets', 'book train tickets']
background_colors = ['BLACK', 'RED', 'GREEN', 'MAGNETA', 'BLUE']
text_colors = ['YELLOW', 'CYAN', 'WHITE', 'YELLOW']
repfr9 = ['your welcome', 'glad i could help you']

while True:
    now = datetime.datetime.now()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tell me something:")
        audio = r.listen(source)
        try:
            print("You said:- " + r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Could not understand audio")
            engine.say('I didnt get that. Rerun the code')

            engine.runAndWait()

    if r.recognize_google(audio) in greetings:
        random_greeting = random.choice(greetings)
        print(random_greeting)
        engine.say(random_greeting)
        engine.runAndWait()

    elif r.recognize_google(audio) in question:
        engine.say('I am fine')
        engine.runAndWait()
        print('I am fine')

    elif r.recognize_google(audio) in var1:
        engine.say('I was made by Atulya')
        engine.runAndWait()
        reply = random.choice(var2)
        print(reply)

    elif r.recognize_google(audio) in cmd9:
        print(random.choice(repfr9))
        engine.say(random.choice(repfr9))
        engine.runAndWait()

    elif r.recognize_google(audio) in cmd7:
        say = random.choice(colrep)
        background = random.choice(background_colors)
        text = random.choice(text_colors)
        init(convert = True)
        print(Fore.YELLOW + Back.RED + text)
        engine.say(text)
        engine.runAndWait()
        print('It keeps changing every micro second')
        engine.say('It keeps changing every micro second')
        engine.runAndWait()

    elif r.recognize_google(audio) in cmd8:
        print(random.choice(colrep))
        engine.say(random.choice(colrep))
        engine.runAndWait()
        print('It keeps changing every micro second')
        engine.say('It keeps changing every micro second')
        engine.runAndWait()

    elif r.recognize_google(audio) in search:
        print('what do you want to search?')
        engine.say('what do you want to search?')
        engine.runAndWait()
        print('SAY>>')
        with sr.Microphone() as source:
            said_audio = r.listen(source)
            try:
                print("You said:- " + r.recognize_google(said_audio))
            except sr.UnknownValueError:
                print("Could not understand audio")
                engine.say('I didnt get that. Rerun the code')

                engine.runAndWait()

            for j in search(str(r.recognize_google(said_audio)), tld="co.in", num=10, stop=10, pause=2):
                print(j)

    elif r.recognize_google(audio) in cmd2:
        mixer.init()
        mixer.music.load("C:\\Users\\Atulya Singh\\Downloads\\Music\\EmptySpaceVevoLiveAcoustic-Arabsong.mp3")
        mixer.music.play()

    elif r.recognize_google(audio) in var4:
        engine.say('I am a bot, silly')
        engine.runAndWait()

    elif r.recognize_google(audio) in cmd4:
        print('What do you want to watch')
        engine.say('What do you want to watch')
        engine.runAndWait()
        print('SAY>>')
        with sr.Microphone() as source:
            said_audio = r.listen(source)
            try:
                print("You said:- " + r.recognize_google(said_audio))
            except sr.UnknownValueError:
                print("Could not understand audio")
                engine.say('I didnt get that.')
                engine.runAndWait()

            webbrowser.open('www.youtube.com/results?search_query='+ r.recognize_google(said_audio))

    elif r.recognize_google(audio) in cmd6:
        print('see you later')
        engine.say('see you later')
        engine.runAndWait()
        exit()

    elif r.recognize_google(audio) in cmd5:
        owm = pyowm.OWM('bc3d02c8c945013259feaf8bb34e6cd2')
        observation = owm.weather_at_place('Jaipur, IN')
        observation_list = owm.weather_around_coords(26.92, 75.82)
        w = observation.get_weather()
        w.get_wind()
        w.get_humidity()
        w.get_temperature('celsius')
        print(w)
        print(w.get_wind())
        print(w.get_humidity())
        print(w.get_temperature('celsius'))
        engine.say(w.get_wind())
        engine.runAndWait()
        engine.say('humidity')
        engine.runAndWait()
        engine.say(w.get_humidity())
        engine.runAndWait()
        engine.say('temperature')
        engine.runAndWait()
        engine.say(w.get_temperature('celsius'))
        engine.runAndWait()

    elif r.recognize_google(audio) in var3:
        print("Current date and time : ")
        print(now.strftime("The time is %H:%M"))
        engine.say(now.strftime("The time is %H:%M"))
        engine.runAndWait()

    elif r.recognize_google(audio) in cmd1:
        webbrowser.open('www.google.com')

    elif r.recognize_google(audio) in cmd3:
        jokrep = random.choice(jokes)
        engine.say(jokrep)
        engine.runAndWait()

    else:
        engine.say("please wait")
        engine.runAndWait()
        print(wikipedia.summary(r.recognize_google(audio)))
        engine.say(wikipedia.summary(r.recognize_google(audio)))
        engine.runAndWait()
        userInput3 = input("or else search in google")
        webbrowser.open_new('www.google.com/search?q=' + r.recognize_google(audio))
