import tornado.ioloop
import tornado.web

# User data
users = {
    'alice': {'Real Name': 'Alice Smith', 'Login': 'alice', 'DOB': 'Jan. 1', 'email': 'alice@example.com'},
    'bob': {'Real Name': 'Bob Jones', 'Login': 'bob', 'DOB': 'Dec. 31', 'email': 'bob@bob.xyz'},
    'carol': {'Real Name': 'Carol Ling', 'Login': 'carol', 'DOB': 'Jul. 17', 'email': 'carol@example.com'},
    'dave': {'Real Name': 'Dave N. Port', 'Login': 'dave', 'DOB': 'Mar. 14', 'email': 'dave@dave.dave'},
}

class ProfileHandler(tornado.web.RequestHandler):
    def get(self, username):
        user = users.get(username)
        if user:
            profile_info = "<br>".join([f"<strong>{key}:</strong> {value}" for key, value in user.items()])
            self.write(f"<h1>User Profile - {username}</h1>{profile_info}")
        else:
            self.write(f"<h1>User {username} not found</h1>")

def make_app():
    return tornado.web.Application([
        (r"/profile/(\w+)", ProfileHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
