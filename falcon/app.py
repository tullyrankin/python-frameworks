import falcon


class IndexResource:
    def on_get(self, req, resp):
        resp.body = "Falcon Index"


class HelloResource:
    def on_get(self, req, resp, user=None):
        user = user or "World"
        resp.body = "Hello {0}!".format(user)

api = falcon.API()
api.add_route('/', IndexResource())
api.add_route('/hello', HelloResource())
api.add_route('/hello/{user}', HelloResource())
