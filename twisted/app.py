from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor


class IndexPage(Resource):
    def render_GET(self, request):
        return "Index Page"


class HelloPage(Resource):
    def render_GET(self, request):
        name = request.args.get("name")
        if type(name) == list and name[0]:
            name = name[0]
        else:
            name = "World"
        return "Hello {0}!".format(name)

root = Resource()
root.putChild("", IndexPage())
root.putChild("hello", HelloPage())
factory = Site(root)
reactor.listenTCP(8080, factory)
reactor.run()
