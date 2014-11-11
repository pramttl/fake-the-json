## Test JSON response generator

Dead simple flask app that takes <60 seconds to install and start a local server to return a test JSON response.

### Instructions

    cd fake-the-json
    sudo pip install -r requirements.txt

Edit "data" dictionary in `app.py` file to edit response. The data variable is a python dictionary that gets converted to a response.

#### Starting server

    # Inside the fake-the-json directory
    python app.py

#### Using service

Send GET or POST request to

    http://localhost:3000/

#### Requirements:

Python 2.7

