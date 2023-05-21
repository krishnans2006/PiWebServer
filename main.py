from flask import Flask, request, session, redirect, url_for
from flask_caching import Cache
from wtforms import Form, StringField, PasswordField, validators

import json
import random
import string


class LoginForm(Form):
    username = StringField("Username", [validators.Length(min=4, max=25), validators.InputRequired()])
    password = PasswordField("Password", [validators.Length(min=6, max=25), validators.InputRequired()])


app = Flask(__name__)

app.config["SECRET_KEY"] = "".join(random.choices(string.ascii_letters, k=10))
print(f"Secret Key: {app.config['SECRET_KEY']}")

cache = Cache(config={"CACHE_TYPE": "SimpleCache"})
cache.init_app(app)


with open("authorized_users.json", "r") as user_file:
    authorized_users = json.load(user_file, parse_int=True)

@app.route("/")
@cache.cached(timeout=100)
def index():
    return "Pi says hi!"


@app.route("/login")
@cache.cached(timeout=10)
def login():
    form = LoginForm(request.data)
    if request.method == "POST" and form.validate():
        session["username"] = form.username.data
        return


@app.route("/logout")
@cache.cached(timeout=10)
def logout():
    session.clear()


@app.route("/dashboard")
@cache.cached(timeout=10)
def dashboard():
    if not session.get("email"):
        return redirect(url_for("login"))


@app.route("/temp")
@cache.cached(timeout=10)
def temp():
    if not session.get("email"):
        return redirect(url_for("login"))
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as file:
        temp = int(file.read().strip())
    return str(temp)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
