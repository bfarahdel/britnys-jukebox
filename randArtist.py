import random


# Randomly pick from the list of artists to select top tracks from
class randArtist:
    def __init__(self, artists):
        if artists == []:
            self.artists = ["Daniela Andrade", "Local Natives", "alt-J"]
        else:
            self.artists = artists

    # Select a random artist from self.artists in __init__
    def pickArtist(self):
        return random.choice(self.artists)
