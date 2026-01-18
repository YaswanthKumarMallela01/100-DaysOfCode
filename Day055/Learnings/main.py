from flask import Flask
import os
print(os.getcwd())
app = Flask(__name__)


@app.route("/")
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>This is a Paragraph</p>'
            '<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3k_XuAG9D4ZEGIr2ETVaBGKjyGxgR_YNLCA&s">')


@app.route("/bye")
def bye():
    return "Bye"


@app.route("/<name>")
def greet(name):
    return f"Hello {name}"


@app.route("/<name>/<int:number>")
def greet2(name, number):
    return f"Hello {name}, you are {number} years old."


if __name__ == "__main__":
    app.run(debug=True)
