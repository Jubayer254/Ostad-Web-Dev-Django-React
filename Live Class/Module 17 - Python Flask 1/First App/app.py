from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def homepage():
    return "<h1>Hello World</h1>"

@app.route('/flask')
def homepage2():
    return "<h1>Hello from Flask</h1>"

@app.route("/user")
@app.route("/user/<name>")
def usename(name = 'Jubayer'):
    return f"<em>{name}</em>"

@app.route("/posts/<int:post_id>/comments/<int:comment_id>")
def comments(post_id, comment_id):
    return f"<p>Post ID: {post_id} Comment ID: {comment_id}</p>"

@app.route("/welcome")
def welcome():
    extra = 'Wow this is so easy!'
    x = 100
    languages = ['Python', 'Java', 'C++', 'C']
    return render_template("index.html", extra = extra, b = x, languages=languages)

@app.route("/login", methods=['GET', 'POST'])
def login():  
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        error = True
        if username == 'admin' and password == 'admin':
            error = False
            return f'Welcome {username}'
        else:
            return render_template("login.html", error= error)
    return render_template("login.html")

@app.route("/api/countries")
def countries():
    countries = ['Bangladesh', 'USA', 'UK', 'Canada', 'Australia']
    return jsonify({"countries" : countries})

@app.route("/api/tasks")
def tasks():
    response = requests.get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()
    return jsonify(data)

@app.route("/api/task/<int:id>")
def task(id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/todos/{id}')
    data = response.json()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)


