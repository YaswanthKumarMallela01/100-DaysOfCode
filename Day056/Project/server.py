from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

# document.body.contentEditable=true    type this in chrome console and press enter to edit the webpage in chrome itself

