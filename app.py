from flask import Flask, request, jsonify
import pyttsx3
import pywhatkit
import datetime
import wikipedia

app = Flask(__name__)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

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
