from wsgiref.simple_server import make_server
from tg import expose, TGController, AppConfig


class RootController(TGController):
    @expose()
    def index(self):
        return "<h1>Turbo Gears 2 Index</h1>"

    @expose()
    def hello(self, user=None):
        user = user or "World"
        return "Hello {0}!".format(user)


config = AppConfig(minimal=True, root_controller=RootController())

print "Serving on port 8080..."
httpd = make_server('', 8080, config.make_wsgi_app())
httpd.serve_forever()
