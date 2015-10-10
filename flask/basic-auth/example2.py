from flask import Flask
from flask.ext.basicauth import BasicAuth

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'admin'
app.config['BASIC_AUTH_PASSWORD'] = 'secret'

basic_auth = BasicAuth(app)


@app.route('/')
@basic_auth.required
def index():
    return "Flask Index Page"

if __name__ == '__main__':
    app.run()
