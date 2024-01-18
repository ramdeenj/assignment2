from flask import Flask

app = Flask(__name__)

# User data
users = {
    'alice': {'Real Name': 'Alice Smith', 'Login': 'alice', 'DOB': 'Jan. 1', 'email': 'alice@example.com'},
    'bob': {'Real Name': 'Bob Jones', 'Login': 'bob', 'DOB': 'Dec. 31', 'email': 'bob@bob.xyz'},
    'carol': {'Real Name': 'Carol Ling', 'Login': 'carol', 'DOB': 'Jul. 17', 'email': 'carol@example.com'},
    'dave': {'Real Name': 'Dave N. Port', 'Login': 'dave', 'DOB': 'Mar. 14', 'email': 'dave@dave.dave'},
}

@app.route('/profile/<username>')
def profile(username):
    user = users.get(username)
    if user:
        profile_info = "<br>".join([f"<strong>{key}:</strong> {value}" for key, value in user.items()])
        return f"<h1>User Profile - {username}</h1>{profile_info}"
    else:
        return f"<h1>User {username} not found</h1>"

if __name__ == '__main__':
    app.run(debug=True, port=8000)
