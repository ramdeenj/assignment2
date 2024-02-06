import tornado.ioloop
import tornado.web
from updateprofile import UpdateProfileHandler

def make_app():
    return tornado.web.Application([
        (r"/updateprofile", UpdateProfileHandler),
        # Add other routes as needed
    ], static_path='static')

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
