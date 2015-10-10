from klein import Klein
app = Klein()


@app.route('/')
def index(request):
    return 'Klein Index Page'


@app.route('/hello')
@app.route('/hello/<user>')
def hello(request, user='World'):
    return 'Hi %s!' % (user,)

app.run("localhost", 8080)
