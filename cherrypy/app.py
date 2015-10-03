import cherrypy


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Index Page"

    @cherrypy.expose
    def hello(self, name="World"):
        return "Hello {0}!".format(name)


cherrypy.quickstart(HelloWorld())
