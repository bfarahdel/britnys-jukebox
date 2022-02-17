from artistSearch import artistSearch


class validateArtist:
    def __init__(self, artistList):
        self.artistList = artistList

    # Remove duplicate artist names
    def removeDup(self):
        uniq = set()
        artists = []
        for artist in self.artistList:
            if artist.lower() not in uniq:
                uniq.add(artist.lower())
                artists.append(artist)
        return artists

    # Validate if the artist appear's in the search results
    def checkArtists(self):
        artists = validateArtist.removeDup(self)
        for artist in artists:
            results = artistSearch(artist).artistResults()
            if results["artistFound"] == False:
                # If an artist is not found in the search results, remove it from the artists list
                artists.remove(artist)
        return artists
