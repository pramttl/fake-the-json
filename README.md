## Test JSON response generator

Dead simple flask app that takes <60 seconds to install and start a local server to return a test JSON response.

### Instructions

Edit "data" dictionary in `app.py` file to edit response. The data variable is a python dictionary that gets converted to a response.

#### Starting server

    cd fake-the-json
    python app.py

#### Using service

Send GET or POST request to

    http://localhost:3000/

#### Requirements:

Python 2.7

