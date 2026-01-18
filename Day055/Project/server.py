from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def home():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">')


num = random.randint(1, 10)
print(num)


@app.route("/<int:number>")
def check(number):
    if number > num:
        return ('<h1>Too High! Try again</h1>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">')
    elif number < num:
        return ('<h1>Too Low! Try again</h1>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')
    return ('<h1>You found me</h1>'
            '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')


if __name__ == "__main__":
    app.run(debug=True)

