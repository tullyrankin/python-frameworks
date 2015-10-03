from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def index(request):
    return Response('Pyramid Index Page')


def hello_world(request):
    return Response('Hello %(name)s!' % request.matchdict)


if __name__ == '__main__':
    config = Configurator()
    config.add_route('index', '/')
    config.add_route('hello', '/hello/{name}')
    config.add_view(index, route_name='index')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
