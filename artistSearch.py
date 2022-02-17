from spTrack import spTrack
from gTrack import gTrack
from randArtist import randArtist

### Process Results from Spotify and Genius API to Flask based on the artist search request from Flask
class artistSearch:
    def __init__(self, artistSubmit):
        self.artistSubmit = artistSubmit  # artist name submitted into the search bar

    # Searches the artist in Spotify then searches the name of the track in Genius
    def artistResults(self):
        artistSearch = spTrack().searchArtist(self.artistSubmit)
        artistFound = (
            True  # will be False if an artist is not found in the search results
        )
        if not artistSearch:
            # Artist did not appear in search results, generate random artist
            artistFound = False
            genArtist = randArtist([]).pickArtist()
            artistSearch = spTrack().searchArtist(genArtist)
        trackLyrics = gTrack().trackLyrics(
            artistSearch["trackArtist"], artistSearch["trackName"]
        )
        artistSearch["trackLyrics"] = trackLyrics
        artistSearch["artistFound"] = artistFound
        return artistSearch
        # Jinja will be used to index from the artistSearch dictionary to display the information in index.html
