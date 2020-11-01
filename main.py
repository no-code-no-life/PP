from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "hello"


@app.route("/api/v1/hello-world-<int:post_id>")
def hello_world(post_id):
    return "Hello World! %d" % post_id


if __name__ == "__main__":
    app.run()
#      gunicorn --bind 0.0.0.0:5000 main:app