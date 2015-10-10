import base64

import cyclone.web
from twisted.internet import reactor


def _checkAuth(username, password):
    '''Check user can access or not to this element'''
    if username == 'admin' and password == 'secret':
        return {'username': username, 'password': password}
    return False


def httpauth(handler_class):
    '''Handle HTTP Basic Auth'''
    def wrap_execute(handler_execute):
        def require_auth(handler, kwargs):
            auth_header = handler.request.headers.get('Authorization')

            if auth_header is None or not auth_header.startswith('Basic '):
                handler.set_status(401)
                handler.set_header('WWW-Authenticate',
                                   'Basic realm=Restricted')
                handler._transforms = []
                handler.finish()
                return False

            auth_decoded = base64.decodestring(auth_header[6:])
            username, password = auth_decoded.split(':', 2)
            auth_found = _checkAuth(username, password)

            if auth_found is False:
                handler.set_status(401)
                handler.set_header('WWW-Authenticate',
                                   'Basic realm=Restricted')
                handler._transforms = []
                handler.finish()
                return False
            else:
                handler.request.headers.add('auth', auth_found)

            return True

        def _execute(self, transforms, *args, **kwargs):
            if not require_auth(self, kwargs):
                return False
            return handler_execute(self, transforms, *args, **kwargs)

        return _execute

    handler_class._execute = wrap_execute(handler_class._execute)
    return handler_class


@httpauth
class MainHandler(cyclone.web.RequestHandler):
    def get(self):
        self.write("Cyclone Index Page")


if __name__ == '__main__':
    application = cyclone.web.Application([
        (r'/', MainHandler),
    ])
    reactor.listenTCP(8000, application)
    reactor.run()
