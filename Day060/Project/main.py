from flask import Flask, render_template, request
import requests
import certifi
import smtplib
import os

app = Flask(__name__)

URL = "https://api.npoint.io/c790b4d5cab58020d391"


def fetch_posts():
    try:
        response = requests.get(URL, verify=certifi.where(), timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Error fetching posts:", e)
        return []


@app.route('/')
def get_all_posts():
    posts = fetch_posts()
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=os.getenv("MY_EMAIL"), password=os.getenv("MY_PASSWORD"))
        connection.sendmail(from_addr=os.getenv("MY_EMAIL"), to_addrs=os.getenv("MY_EMAIL"), msg=email_message)


@app.route("/post/<int:index>")
def show_post(index):
    posts = fetch_posts()
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
            break
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
