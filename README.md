# Britny's Jukebox

A website hosted on [Heroku](https://www.heroku.com/) and developed with the Python [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework and [React](https://reactjs.org/) framework that utilizes [Spotipy](https://spotipy.readthedocs.io/en/2.19.0/) (a Python library for the Spotify API) to select a top track from artists saved by the user in a [Heroku PostgreSQL](https://devcenter.heroku.com/articles/heroku-postgresql) database and display the following information on the top track of an artist based on Spotify's ranking:

- Artist name
- Track name
- Cover art
- Names of 3 similar artists
- Audio player that plays a 30 second preview of the track
  <br></br>

A link to the lyrics page hosted on [Genius](https://genius.com) is also provided. The [Genius API](https://docs.genius.com/) is used to search for the lyrics of the top track from the [Spotify API](https://developer.spotify.com/documentation/web-api/).
<br></br>
**Website URL**: https://reactbritnysjukebox.herokuapp.com/
<br></br>
When accessing the website intially, the login page will be displayed on the website. The user can either login or sign up. In order to sign up on the website, the user must enter a username and password between **6 to 12 characters** in length and will be notified if these specifications are not met. Duplicate usernames are **not** allowed and the user will be notified if the username already exists in the database. The **password** is **encrypted**.
<br></br>
Following a successful login, a random top track (based on its popularity in Spotify) from one of the user's saved artists will be displayed on the website. If the user does not have any artists saved, a random top track from one of 3 artists (Adele, alt-J, Koethe) will be displayed on the website. The user can either **add** or **delete** artists to and from the saved artists list. The user can then click **Save** to update the saved artists list in the database. The artist's name is **case-insensitive** meaning that it will be saved regardless of whether the user types the artist's name in uppercase or lowercase, but it will be added to the database as specified by the user input in the text box. Duplicates will automatically be removed and only **one** instance of the artist name will appear. Each artist name in the artist list requested to be saved by the user will have its search results **validated** with Spotify. If an artist name gives no search results, it will automatically be removed from the list.
<br></br>

## Running the Application

After meeting the requirements in the **Getting Started** section, install the node modules using the command `npm install` (this only needs to be done once for initial setup). After installation, this application can be run in two ways:

1. Running the shell script included in the repository in the current directory:

```
./launchApp.sh
```

2. Run the following lines in the terminal:

```
npm run build
python3 app.py
```

## Getting Started

The following is necessary in order to to run this application when cloning the repository:

- Python [installation](https://www.python.org/downloads/)
- Python [Flask](https://flask.palletsprojects.com/en/2.0.x/) framework
  - Can be installed using the following command: `pip install Flask`
- [Spotipy](https://spotipy.readthedocs.io/en/2.19.0/) library
  - Can be installed using the following command: `pip install spotipy`
- [.env](https://pypi.org/project/python-dotenv/) file containing the client id and client secret keys from Spotify, the Client Access Token from Genius, the application secret key, and the URL to access the PostgreSQL database.
  - The .env configuration variables can be accessed using the [python-dotenv](https://pypi.org/project/python-dotenv/) library (can be installed using the following command: `pip install python-dotenv`)
- Python [requests](https://docs.python-requests.org/en/latest/) library allows the application to send an HTTP/1.1 request to the API service from the client using the set of API keys in the .env file.
  - Can be installed using the following command: `pip install requests`

### Required to work with the Heroku Database

- Python [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) is a Flask extension that provides support for SQLAlchemy.
  - Can be installed using the following command: `pip install Flask-SQLAlchemy==2.1`
- Python [psycopg2-binary](https://www.psycopg.org/docs/install.html) is a database adapter that allows management of database interactions.
  - Installation: `pip install psycopg2-binary`
- Python [flask_login](https://flask-login.readthedocs.io/en/latest/) provides user session management for user authentication.
  - Installation: `pip install flask-login`

### .env File Configuration

To ensure the web application has all the environment variables it needs to run, make sure to set up the following variables:

- Spotify API
  - sp_clientID
  - sp_clientSecret
- Genius API
  - g_tok
- Necessary for the PostgreSQL database
  - appSecret
    - Can be generated using the Python os library
    ```
    import os
    os.urandom(12)
    ```
  - DATABASE_URL
    - From the Heroku database configuration

## Spotipy (a Python library for the Spotify API)

A client id and client secret key from the [registered app](https://developer.spotify.com/dashboard/applications) (requires sign up for a Spotify account) in the Spotify API are used to authenticate requests to the Spotify Web API using the Client Credentials flow. The client id and client secret key are stored in the .env file of the project (located in .gitignore for security purposes). When cloning this repository, a .env file should be created and should include a client id and client secret key from the Spotify API. The [Spotipy](https://spotipy.readthedocs.io/en/2.19.0/) python library is utilized to obtain track information for the artist specified by the user.

## Genius API

To use the Genius API, a Client Access Token needs to be obtained when creating a ["New API Client"](https://genius.com/api-clients) (requires sign up for a Genius account). The Client Access Token is stored in the .env file of the project (located in .gitignore for security purposes). When cloning this repository, a .env file should be created and should include a Client Access Token from Genius.

## Heroku

The web application and database are hosted on Heroku, a cloud platform as a service (PaaS). Please note that the web application and database are two separate Heroku applications. All [config vars](https://devcenter.heroku.com/articles/config-vars) (Spotify API client id and client secret, Genius API Client Access Token, application secret, postgresql database url) from the .env file must be specified in Heroku. A [requirements.txt](https://devcenter.heroku.com/articles/python-support) file should also be included with the libraries used in the application. One additional file, named exactly as [Procfile](https://devcenter.heroku.com/articles/procfile) without a file extension is required to declare process types for the application to be deployed into Heroku. More information on creating a PostgreSQL database in Heroku can be found [here](https://devcenter.heroku.com/articles/heroku-postgresql).

## PostgreSQL Database

Prior to using the application, the database model must be created from `main.py`. To do this, in run the following commands in an interactive Python shell:

```
from main import db
db.create_all()
```

More information can be found on the Flask-SQLAlchemy [quickstart](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/) page