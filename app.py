from flask import Flask, request, jsonify
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

app = Flask(__name__)

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

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

def run_sweety(command):
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
        return f'Playing {song}'
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('current time is' + time)
        return f'Current time is {time}'
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 2)
        talk(info)
        return info
    elif 'how are you' in command:
        talk('I am good as always. By the way, how is your crush?')
        return 'I am good as always. By the way, how is your crush?'
    else:
        talk('Please say that again.')
        return 'Please say that again.'

@app.route('/ask_sweety', methods=['POST'])
def ask_sweety():
    data = request.get_json()
    command = data.get('message')
    response = run_sweety(command)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
