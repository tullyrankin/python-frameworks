# Tornado Web Framework
Tornado is a Python web framework and asynchronous networking library, originally developed at FriendFeed. By using non-blocking network I/O, Tornado can scale to tens of thousands of open connections, making it ideal for long polling, WebSockets, and other applications that require a long-lived connection to each user. http://www.tornadoweb.org/en/stable/

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
