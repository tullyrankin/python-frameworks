import bottle


def check(user, password):
    if user == 'admin' and password == 'secret':
        return True
    return False


@bottle.route('/')
@bottle.auth_basic(check)
def index():
    return 'Bottle Index Page'


if __name__ == '__main__':
    print 'Starting server...'
    bottle.run(host='127.0.0.1', port=8080, reloader=True)
