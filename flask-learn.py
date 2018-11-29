from flask import Flask, render_template, request
import requests
import os
app = Flask("MyApp")

def send_simple_message(email):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox9b397e46f7ab40d09d0d99d0adb827c6.mailgun.org/messages",
        auth=("api", "d77a01c8ff4d9d31f456a6f9e59ca67f-9525e19d-4356b605"),
        data={"from": "Excited User <mailgun@sandbox9b397e46f7ab40d09d0d99d0adb827c6.mailgun.org>",
              "to": [email],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})


@app.route("/")
def hello():
    return "Hello World"

@app.route("/<name>")
def hello_someone(name):
        return render_template("hello.html", name=name.title())

@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    email = form_data["email"]
    send_simple_message(email)
    return "Email Sent to: {}".format(email)

app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
