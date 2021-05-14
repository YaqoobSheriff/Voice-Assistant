import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.say("This is Tommy  ")
engine.runAndWait()

def talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            value = listener.recognize_google(voice)
            value = value.lower()
            if 'Tommy' in value:
                value = value.replace('Tommy', '')
                print(value)
    except:
        pass
    return value


def run_gundu():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'repeat' in command:
        content = command.replace('repeat', '')
        talk(content)
    elif 'exit' in command:
        talk('Exiting....')
        exit()
    else:
        talk('Please say the command again.')

while True:
    run_gundu()

