# Get it cause it's WSGI in the jar

from flask_server import app

from waitress import serve


serve(app, host='0.0.0.0', port=80)