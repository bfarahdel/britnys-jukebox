from flask.helpers import url_for
from flask_login.utils import login_required
from werkzeug.utils import redirect
from randArtist import randArtist
from artistSearch import artistSearch
from validateArtist import validateArtist
from flask import request, render_template, Flask, flash, Blueprint, jsonify
import os
from dotenv import find_dotenv, load_dotenv
from flask_login import current_user, UserMixin, LoginManager, login_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON

# sha256 hash for the user's password
from werkzeug.security import generate_password_hash, check_password_hash
import json

load_dotenv(find_dotenv())

app = Flask(__name__, static_folder="./build/static")

app.secret_key = os.getenv("appSecret")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

### Database
db = SQLAlchemy(app)


class Person(UserMixin, db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(1000))
    artists = db.Column(JSON)


### flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def user_loader(user_id):
    return Person.query.get(int(user_id))


# This tells our Flask app to look at the results of `npm build` instead of the
# actual files in /templates when we're looking for the index page file. This allows
# us to load React code into a webpage. Look up create-react-app for more reading on
# why this is necessary.
bp = Blueprint("bp", __name__, template_folder="./build")


@bp.route("/index")
@login_required
def index():
    query = Person.query.filter_by(username=current_user.username).first()
    pArtists = query.artists["artists"]

    pArtists.sort()

    inArtist = artistSearch(randArtist(pArtists).pickArtist()).artistResults()
    # a random artist will be selected from the user's saved artists
    # if the user does not have any artists saved, a random artist will be selected from the list of 3 artists in randArtist.py

    DATA = {
        "getUser": current_user.username,
        "pArtists": pArtists,
        "trackArtist": inArtist["trackArtist"],
        "trackName": inArtist["trackName"],
        "trackRelated": inArtist["trackRelated"],
        "trackCover": inArtist["trackCover"],
        "trackAudio": inArtist["trackAudio"],
        "trackLyrics": inArtist["trackLyrics"],
    }
    data = json.dumps(DATA)

    return render_template(
        "index.html",
        data=data,
    )


app.register_blueprint(bp)


@app.route("/")
def main():
    if current_user.is_authenticated:
        return redirect(url_for("bp.index"))
    return redirect(url_for("login"))


@app.route("/appArtists", methods=["POST"])
def appArtists():
    app_artists = request.get_json("artists")
    artistList = app_artists["artists"]

    if app_artists:
        if "artists" in app_artists:
            # Validate artists
            artistValid = validateArtist(artistList).checkArtists()

            # No artists failed validation
            # Update the saved artists list for the user in the database
            query = Person.query.filter_by(username=current_user.username).first()
            pUpdate = Person(
                username=current_user.username,
                password=current_user.password,
                artists={"artists": artistValid},
            )
            db.session.delete(query)
            db.session.commit()
            db.session.add(pUpdate)
            db.session.commit()
            login_user(pUpdate)

    return jsonify({"appArtists_server": artistValid})


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    username = request.form["username"]
    password = request.form["password"]
    dbUser = Person.query.filter_by(username=username).first()
    if dbUser:
        if username == dbUser.username:
            # if the user exists in the database then check the password
            if check_password_hash(dbUser.password, password):
                login_user(dbUser)
                return redirect(
                    url_for("bp.index")
                )  # go to the jukebox page if the user's password matches the password in the database
    flash("Login failed.")
    return render_template("login.html")


@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    username = request.form.get("username")
    password = request.form.get("password")
    if username and password:
        # Ensure the length of username and password is between 6 and 12 characters
        if (len(username) < 6 or len(username) > 12) and (
            len(password) < 6 or len(password) > 12
        ):
            flash("Username and password must be between 6 and 12 characters.")
        elif len(username) < 6 or len(username) > 12:
            flash("Username must be between 6 and 12 characters.")
        elif len(password) < 6 or len(password) > 12:
            flash("Password must be between 6 and 12 characters.")
        else:
            # Check if user exists in the database before adding the user
            pCheck = Person.query.filter_by(username=username).first()
            if pCheck is None:
                add_user = Person(
                    username=username,
                    password=generate_password_hash(password),
                    artists={"artists": []},
                )
                # add the user to the database
                db.session.add(add_user)
                db.session.commit()
                return redirect(
                    url_for("login")
                )  # the user will be redirected to the login page after signing up
            else:
                flash("That username already exists. Please use a different username.")
    else:
        flash("Sign up was unsuccessful. Please enter a username and password.")
        redirect(url_for("signup"))

    return render_template("signup.html")


app.run(
    host=os.getenv("IP", "0.0.0.0"),
    port=int(os.getenv("PORT", 8081)),
)
