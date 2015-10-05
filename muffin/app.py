import muffin


app = muffin.Application('example')


@app.register('/')
def index(request):
    return "Muffin Index"


@app.register('/hello', '/hello/{name}')
def hello(request):
    name = request.match_info.get('name', 'World')
    return 'Hello {0}!'.format(name)
