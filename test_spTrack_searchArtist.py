import unittest
from unittest.mock import patch
from spTrack import spTrack


# Tests the case when an artist is not found from Spotify (INPUT is an empty string). None should be returned.
INPUT = "artist_names"
EXPECTED_OUTPUT = "expected"


class searchArtist_test(unittest.TestCase):
    def setUp(self):
        self.test_params = [
            {
                INPUT: "",
                EXPECTED_OUTPUT: None,
            },
            {
                INPUT: "The Beatles",
                EXPECTED_OUTPUT: {
                    "trackArtist": "The Beatles",
                    "trackName": "track",
                    "trackAudio": "audio",
                    "trackCover": "cover",
                    "trackRelated": "The Beatles_related",
                },
            },
            {
                INPUT: "Ariana Grande",
                EXPECTED_OUTPUT: {
                    "trackArtist": "Ariana Grande",
                    "trackName": "track",
                    "trackAudio": "audio",
                    "trackCover": "cover",
                    "trackRelated": "Ariana_related",
                },
            },
        ]

    def test_search(self):
        for test in self.test_params:
            with patch("spTrack.spTrack.searchArtist"):
                if test[INPUT] == "":
                    spTrack.searchArtist = None
                    self.assertEqual(spTrack.searchArtist, test[EXPECTED_OUTPUT])
                else:
                    spTrack.searchArtist = test[
                        EXPECTED_OUTPUT
                    ]  # What was found in the search results
                    print(spTrack.searchArtist)
                    self.assertIsNotNone(spTrack.searchArtist)


if __name__ == "__main__":
    unittest.main()
