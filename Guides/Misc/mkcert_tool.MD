This is a tool designed to create a certificate for a Web browser

First, create a new Flask app.
; mkdir secure_flask
; cd secure_flask
; pipenv install --python 3.11 flask
; pipenv shell
; touch app.py

# File: app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run(port=4321)


Now install by doing the following:
; brew install mkcert
; mkcert -install
# This will install a root certificate on your computer so that you can trust
# certificates created by mkcert.
# You can ignore "ERROR: no Firefox security database found" if you see it.
; mkcert localhost
# This will create a certificate pair valid for localhost and store them in
# `localhost.pem` and `localhost-key.pem`. You can take a look at them if you
# like.

Now let's configure our Flask app to use the certificate:

# Replace the two lines at the end of `app.py` with these:
if __name__ == '__main__':
    app.run(port=4321, ssl_context=('localhost.pem', 'localhost-key.pem'))

Retstart the server 
; python app.py
; open https://localhost:4321/


If you get this site cant be reached 

Make sure you've got https at the start of the url with the s. It won't work if you haven't.

