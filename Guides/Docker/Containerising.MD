************TWEEKING FLASK********************

You'll need to make a couple tweaks to your Flask app to make it run properly in a container. This isn't unusual — most software does need a few adjustments to prepare it for deployment.

The key change for us is to app.py in the section where you run the flask server. Yours might look like this:

if __name__ == '__main__':
    app.run(debug=True)
Or you might not have it at all! In any case, you'll need one and for it to look like this:

if __name__ == '__main__':
    app.run(
      debug=True, # Optional but useful for now
      host="0.0.0.0" # Listen for connections directed _to_ any address
    )
The host="0.0.0.0" option tells Flask to listen for connections that are directed to any IP address (think of 0.0.0.0 as a wildcard) as opposed to just the ones coming to localhost 127.0.0.1. We need this because the container's new localhost is just going to be connections from inside the container. We're outside the container, so we need to tell it to listen more generally.

If you can run this and see roughly this output you're in a good place:

; pipenv run python app.py
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.8.115:5000 # Note the second IP address here
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 738-310-080

************CONTAINERISING******************************

# Imagine this file as a recipe for setting up a virtual computer.

# Dockerfiles typically start with a 'base image'. There are loads of these
# and you can find them at hub.docker.com.
# We're going to use a base image for Python version 3.11
FROM python:3.11

# This base image contains essentially everything necessary for a 'virtual
# computer'. It has a terminal, certain basic commands, and of course Python.

# We run a command to install `pipenv`
RUN pip install pipenv

# We'll need our app's files in the container in order to be able to run them!
# We copy them in from the current directory to the folder `/app` in
# our virtual computer. Reminder `.` means 'the current directory'
COPY . /app

# We set the working directory for commands from this point on
WORKDIR /app

# We run `pipenv install` to install our project's dependencies. Since we've
# copied in our `Pipfile`, `pipenv` will use that to get a list of dependencies.
# We include a couple of extra options suitable for deployment.
RUN pipenv install --system --deploy

# At this point we've set up our virtual computer, but we've not _yet_ run our
# application. And we're not going to! We're just setting up the container
# so that it's ready to do so when we tell it.

# So we're going to tell Docker here that when we _do_ want to run it, this is
# what it should run:
CMD ["python", "app.py"]

*******GETTING DOCKER TO BUILD THE IMAGE**********

make sure docker is running in the background
run the following: docker build --tag < name the image you want to build .>


*******RUNNING THE CONTAINER***********

Run the following to run the container: 
docker run --publish < Host comp port : container port > < image name >
  Note:
    the host comp port is the port you will have to vist to see the file