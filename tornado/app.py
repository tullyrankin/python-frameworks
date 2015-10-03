import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Tornado Index Page")


class HelloHandler(tornado.web.RequestHandler):
    def get(self, name):
        if not name:
            name = "World"
        self.write("Hello {0}!".format(name))

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/hello/?(.*)", HelloHandler),
])

if __name__ == "__main__":
    application.listen(8080)
    tornado.ioloop.IOLoop.current().start()
