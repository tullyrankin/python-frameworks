# Klein Web Framework
Klein is a micro-framework for developing production-ready web services with Python. 
It is 'micro' in that it has an incredibly small API similar to Bottle and Flask. 
It is not 'micro' in that it depends on things outside the standard library. 
This is primarily because it is built on widely used and well tested components like Werkzeug and Twisted.

Github: https://github.com/twisted/klein

Documentation: http://klein.readthedocs.org/

## Routes
```/``` - Index Page

```/hello``` - Hello World!

```/hello/<user>``` - Hello <user>!

## Local Installation
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

## Start The Server
```
python app.py
```
