import unittest
from randArtist import randArtist

INPUT = "artist_lists"
EXPECTED_OUTPUT = "expected"


class randArtist_test(unittest.TestCase):
    def setUp(self):
        self.test_params = [
            {INPUT: ["The Rolling Stones"], EXPECTED_OUTPUT: ["The Rolling Stones"]},
            {INPUT: ["The Beatles"], EXPECTED_OUTPUT: ["The Beatles"]},
            {INPUT: [], EXPECTED_OUTPUT: ["Adele", "Koethe", "alt-J"]},
        ]
        self.artists = [
            {INPUT: ["The Rolling Stones"], EXPECTED_OUTPUT: ["The Rolling Stones"]},
            {INPUT: ["The Beatles"], EXPECTED_OUTPUT: ["The Beatles"]},
        ]

    # Given an artist name in a list, the artist name is expected.
    # If the list is empty, then it should return the random artist list
    def test_list_randArtist(self):
        for test in self.test_params:
            actualArtists = randArtist(test[INPUT]).artists
            expectedArtists = test[EXPECTED_OUTPUT]
            self.assertEqual(actualArtists, expectedArtists)

    # Ensure that a random artist is not selected given an artist input
    def test_artist_randArtist(self):
        for test in self.artists:
            actualArtists = randArtist(test[INPUT]).pickArtist()
            randArtists = ["Adele", "Koethe", "alt-J"]
            self.assertNotEqual(actualArtists, randArtists)


if __name__ == "__main__":
    unittest.main()
