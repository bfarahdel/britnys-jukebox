import requests
from dotenv import find_dotenv, load_dotenv
import os


### Genius API
# Accesses the Genius API with the authorization token
class gTrack:
    load_dotenv(find_dotenv())

    def __init__(self):
        self.g_tok = os.getenv("g_tok")

    # Returns the URL of the lyrics for the name of a track
    def trackLyrics(self, trackArtist, trackName):
        # Search for the song in Genius with the name of the artist and track obtained from Spotify
        browseURL = f"http://api.genius.com/search?q={trackArtist} {trackName}&access_token={self.g_tok}"

        response = requests.get(url=browseURL)
        response_json = response.json()

        if response_json:
            Numlyrics = len(response_json["response"]["hits"])
            if Numlyrics < 1:  # if at least 1 set of lyrics are not found return null
                return None

            # return url of the lyrics page at the top of the search results
            lyricsURL = response_json["response"]["hits"][0]["result"]["url"]
        else:
            lyricsURL = None

        return lyricsURL
