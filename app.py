import logging

from flask import Flask
from flask_ask import Ask, question, statement
logging.getLogger('flask_ask').setLevel(logging.DEBUG)


app = Flask('__name__')
ask = Ask(app, '/')


@ask.launch
def launch():
    speech_text = 'Welcome to my alexa skill set'
    return question(speech_text). \
        reprompt(speech_text). \
        simple_card('HelloWorld', speech_text)


@ask.intent('HelloWorldIntent')
def hello_world():
    speech_text = 'Hello world'
    return statement(speech_text).simple_card('HelloWorld', speech_text)


@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = 'You can say hellow to me'
    return question(speech_text). \
        reprompt(speech_text). \
        simple_card('HelloWorld', speech_text)


@ask.session_ended
def session_ended():
    return "", 200


if __name__ == '__main__':
    app.run(debug=True)
