import tornado.ioloop
import tornado.web

# User data
users = {
    'alice': {'Real Name': 'Alice Smith', 'Login': 'alice', 'DOB': 'Jan. 1', 'email': 'alice@example.com', 'image': '/static/alice.jpg'},
    'bob': {'Real Name': 'Bob Jones', 'Login': 'bob', 'DOB': 'Dec. 31', 'email': 'bob@bob.xyz', 'image': '/static/bob.jpg'},
    'carol': {'Real Name': 'Carol Ling', 'Login': 'carol', 'DOB': 'Jul. 17', 'email': 'carol@example.com', 'image': '/static/carol.jpg'},
    'dave': {'Real Name': 'Dave N. Port', 'Login': 'dave', 'DOB': 'Mar. 14', 'email': 'dave@dave.dave', 'image': '/static/dave.jpg'},
}

class ProfileHandler(tornado.web.RequestHandler):
    def get(self, username):
        user = users.get(username)
        if user:
            profile_info = "<br>".join([f"<strong>{key}:</strong> {value}" for key, value in user.items()])
            self.write(f"""
                <html>
                <head>
                    <link rel="stylesheet" type="text/css" href="/static/styles.css">
                </head>
                <body>
                    <div class="profile-container">
                        <img src="{user['image']}" alt="{username}'s Profile Picture">
                        <h1>User Profile - {username}</h1>
                        {profile_info}
                    </div>
                </body>
                </html>
            """)
        else:
            self.write(f"<h1>User {username} not found</h1>")

def make_app():
    return tornado.web.Application([
        (r"/profile/(\w+)", ProfileHandler),
        (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "static"}),
    ], template_path='templates', static_path='static')

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
