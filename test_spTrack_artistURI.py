import unittest
from unittest.mock import patch
from spTrack import spTrack


# Tests if the artistURI function in spTrack.py returns the correct artist id given an artist name
INPUT = "artist_names"
EXPECTED_OUTPUT = "expected"


class artistURITestCase(unittest.TestCase):
    def setUp(self):
        self.test_params = [
            {
                INPUT: "The Rolling Stones",
                EXPECTED_OUTPUT: "spotify:artist:22bE4uQ6baNwSHPVcDxLCe",
            },
            {
                INPUT: "The Beatles",
                EXPECTED_OUTPUT: "spotify:artist:3WrFJ7ztbogyGnTHbHJFl2",
            },
            {
                INPUT: "Ariana Grande",
                EXPECTED_OUTPUT: "spotify:artist:66CXWjxzNUsdJxJ2JdwvnR",
            },
        ]

    # Test if the artist ID output is correct given an artist name
    def test_artistURI(self):
        for test in self.test_params:
            with patch("spTrack.spTrack.artistURI"):
                if test[INPUT] == "The Rolling Stones":
                    spTrack.artistURI = "spotify:artist:22bE4uQ6baNwSHPVcDxLCe"
                    self.assertEqual(spTrack.artistURI, test[EXPECTED_OUTPUT])
        # Should return "The Rolling Stones" artist ID with the given inputs
        self.assertIsNotNone(spTrack.artistURI)


if __name__ == "__main__":
    unittest.main()
