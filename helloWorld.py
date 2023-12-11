# File: app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

#The below runs without a certificate

#if __name__ == '__main__':
#    app.run(port=5001)

# The below runs the app with a certificate
if __name__ == '__main__':
    app.run(port=5001, ssl_context=('localhost.pem', 'localhost-key.pem'))