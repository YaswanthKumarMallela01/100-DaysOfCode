import datetime
from flask import Flask, render_template
import random
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    """Rendering index.html by parsing those 2 parameters which can be used to run python scripts
    from html."""
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    response = requests.get(gender_url)
    gender = response.json()["gender"]

    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age = age_response.json()["age"]

    return render_template("guess.html", gen_gender=gender, gen_age=age, name=name)


@app.route("/blog")
def get_blog():
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url)
    return render_template("blog.html", all_blogs=response.json())


if __name__ == "__main__":
    app.run(debug=True)
