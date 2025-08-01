"""
This script runs the FlaskWebProject application using a development server.
"""

from os import environ
from FlaskWebProject import app
import logging

if __name__ == '__main__':
    app.debug = True
    HOST = environ.get('SERVER_HOST', '0.0.0.0')  # Use 0.0.0.0 to accept external connections
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    # Run with HTTPS using adhoc self-signed cert
    app.run('0.0.0.0', PORT, ssl_context='adhoc')

