from flask import Flask, render_template, request

import requests

app = Flask(__name__)

@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    print form_data["email"]
    return "Thank you for joining Blue Planet"

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox828fb5c2d473486993dbc11697fe59f1.mailgun.org/messages",
        auth=("api", "bba4b1d069e2239ab9459f269eb6932b-39bc661a-4b83dccf"),
        data={"from": "Excited User <mailgun@sandbox828fb5c2d473486993dbc11697fe59f1.mailgun.org>",
              "to": ["irisccgoncalves@gmail.com", "aleksandrajasik16@gmail.com"],
              "subject": "Welcome to Our Blue Planet",
              "text": "Thank you for joining Blue Planet. We will be in touch with your shortly to give you access to future events. Stay tuned!"})

send_simple_message()

app.run(debug=True)
