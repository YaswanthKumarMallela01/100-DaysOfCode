from flask import Flask
import random
app = Flask(__name__)   # __name__ = __main__
print(random.__name__)  # Prints the name of the package
print(__name__)


@app.route("/")         # Python Decorator to root page
def hello_world():
    return "<h1>Hello, World!</h1>"


@app.route("/bye")      # Python decorator for 'bye' page
def bye():
    return "Bye"


if __name__ == "__main__":
    app.run()
