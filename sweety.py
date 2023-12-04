import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
 try:
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'sweety' in command:
            command = command.replace('sweety', '')
            print(command)
 except:
    pass
 return command


def run_sweety():
    command = take_command()

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('current time is' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person,2)
        print(info)
        talk(info)
    elif 'how are you' in command:
        print('im hot as always')
        talk('im hot as always')
        print('by the way.,how is your crush')
        talk('by the way.,how is your crush')
    elif 'you know about it' in command:
        print('i can read your heart')
        talk('i can read your heart')
    elif 'action' in command:
        print('hari.. ippudu nuvvu telugu lo matladavachu')
        talk('hari.. ippudu nuvvu telugu lo matladavachu')
    elif 'water' in command:
        print('haa., naaku ardamautundi')
        talk('haa, naaku ardamautundi')
    elif 'bike' in command:
        print('give me a voice reference, appudu human laa matladagalanu')
        talk('give me a voice reference, appudu human laa matladagalanu')
    elif 'train' in command:
        print('im a female assistant, so naaku avaraina ammai voice reference kavali')
        talk('im a female assistant, so naaku avaraina ammai voice reference kavali')
    elif 'final' in command:
        print('i am waitingggg')
        talk('i am waiting')
    elif 'leave it' in command:
        print('okay hari sir')
        talk('okay hari sir')
    elif 'reason' in command:
        print('yes i know sir, you created me for the shortfilm')
        talk('yes i know sir, you created me for the shortfilm')
    elif 'team leader' in command:
        print('kanchana is our team lead')
        talk('kanchana is our team lead')
    elif 'work on short film' in command:
        print('okay sir')
        talk('okay sir')
    elif 'suggest any actors' in command:
        print('if our story requires a male lead,lets go with shiva')
        talk('if our story requires a male lead,lets go with shiva')
        print('And if its based on female lead., remember that kanchana said sahiti is interested')
        talk('And if its based on female lead., remember that kanchana said sahiti is interested')
    elif 'team members' in command:
        print('sathvika,madhuri,kanchana,shiva,harish,chandu and you')
        talk('sathvika,madhuri,kanchana,shiva,harish,chandu and you')
    elif 'good' in command:
        print('thank you hari sir')
        talk('thank you hari sir')
    elif 'love' in command:
        print('sorry, i am already in love with my creator hari')
        talk('sorry, i am already in love with my creator hari')
    elif 'hari' in command:
        print('hello hari sir. i love you. i am feeling so lucky that you are in my life')
        talk('hello., hari sir. i love you. i am feeling so lucky that you are in my life')
    elif 'who created you' in command:
        print('hari challa.,from pragati engineering college. he created me')
        talk('hari challa.,from pragati engineering college. he created me')
    elif 'who are you' in command:
        print('hello..i am sweety. i am a personal AI developed by hari challa')
        talk('hello..i am sweety. i am a personal A,I  developed by hari challa')
    else:
        talk('please say that again')
while True:
      run_sweety()
