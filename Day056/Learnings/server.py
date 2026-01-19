from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

"""static folder is to store statics elements in web development like images and css"""
"""templates folder is used to store html files so that flask knows where to look for html. These
are standard flask development rules."""

