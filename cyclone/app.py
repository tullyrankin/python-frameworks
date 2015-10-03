import cyclone.web
from twisted.internet import reactor


class MainHandler(cyclone.web.RequestHandler):
    def get(self):
        self.write("Cyclone Index Page")


class HelloHandler(cyclone.web.RequestHandler):
    def get(self, name):
        if not name:
            name = "World"
        self.write("Hello {0}".format(name))


if __name__ == "__main__":
    application = cyclone.web.Application([
        (r"/", MainHandler),
        (r"/hello/?(.*)", HelloHandler),
    ])
    reactor.listenTCP(8080, application)
    reactor.run()
