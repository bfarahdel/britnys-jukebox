import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import find_dotenv, load_dotenv
import os
import random

### Spotify API
# Accesses the Spotify API with the authorization token
class spTrack:
    load_dotenv(find_dotenv())

    def __init__(self):
        self.clientID = os.getenv("sp_clientID")
        self.clientSecret = os.getenv("sp_clientSecret")
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyClientCredentials(
                client_id=self.clientID,
                client_secret=self.clientSecret,
                requests_session=True,
            ),
            retries=7,
        )

    # Selects a random track from the top tracks of the artist
    def pickTrack(self, uri):
        topTracks = self.sp.artist_top_tracks(uri, country="US")["tracks"]
        trackArtist = self.sp.artist(uri)["name"]
        randTrack = random.randint(
            0, len(topTracks) - 1
        )  # Generate a random index to select a track from topTracks
        trackJSON = topTracks[randTrack]
        trackName = trackJSON["name"]
        trackAudio = trackJSON["preview_url"]
        trackCover = trackJSON["album"]["images"][0]["url"]
        trackRelatedJSON = self.sp.artist_related_artists(
            uri
        )  # Get artists related to the artist searched
        numRelated = len(trackRelatedJSON["artists"])
        if (
            numRelated < 3
        ):  # At most three similar artists found from Spotify will be obtained
            if numRelated == 2:
                trackRelated = f"{trackRelatedJSON['artists'][0]['name']}, {trackRelatedJSON['artists'][1]['name']}"
            elif numRelated == 1:
                trackRelated = f"{trackRelatedJSON['artists'][0]['name']}"
            else:
                trackRelated = None
        else:
            trackRelated = f"{trackRelatedJSON['artists'][0]['name']}, {trackRelatedJSON['artists'][1]['name']}, {trackRelatedJSON['artists'][2]['name']}"
        trackDict = {
            "trackArtist": trackArtist,
            "trackName": trackName,
            "trackAudio": trackAudio,
            "trackCover": trackCover,
            "trackRelated": trackRelated,
        }
        return trackDict

    # Searches for the URI of the artist
    def artistURI(self, artistSearch):
        artistResults = self.sp.search(
            q="artist:" + artistSearch, type="artist", market="US"
        )
        artistItems = artistResults["artists"]["items"]
        if len(artistItems) > 0:  # checks if an artist was found in the search results
            artistFound = artistItems[0]["uri"]
            return artistFound  # returns the URI of the artist

    # Returns the trackArtist, trackName, trackAudio, trackCover, and trackRelated from pickTrack after searching the URI with artistURI
    # in a dictionary
    def searchArtist(self, artistSearch):
        artistFound = spTrack().artistURI(artistSearch)
        if (
            artistFound
        ):  # select a top track if an artist was found in Spotify's search results
            trackDict = spTrack().pickTrack(artistFound)
            return trackDict
