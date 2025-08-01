from os import environ
from FlaskWebProject import app
import logging

if __name__ == '__main__':
    app.debug = True
    HOST = environ.get('SERVER_HOST', '0.0.0.0')  # Change default to 0.0.0.0
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, ssl_context='adhoc')
