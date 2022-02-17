import unittest
from validateArtist import validateArtist

INPUT = "artist_lists"
EXPECTED_OUTPUT = "expected"


class validateArtist_test(unittest.TestCase):
    def setUp(self):
        self.valid_params = [
            {
                INPUT: ["The Rolling Stones", "Ariana Grande", "the rolling stones"],
                EXPECTED_OUTPUT: ["The Rolling Stones", "Ariana Grande"],
            },
            {INPUT: ["The Beatles"], EXPECTED_OUTPUT: ["The Beatles"]},
            {INPUT: [], EXPECTED_OUTPUT: []},
        ]
        self.check_is = [
            {
                INPUT: ["The Rolling Stones", "Taylor Swift"],
                EXPECTED_OUTPUT: ["The Rolling Stones", "Ariana Grande"],
            }
        ]

    def test_list_validateArtist(self):
        for test in self.valid_params:
            actualArtists = validateArtist(test[INPUT]).removeDup()
            expectedArtists = test[EXPECTED_OUTPUT]
            self.assertEqual(actualArtists, expectedArtists)

    def test_check_is(self):
        for test in self.check_is:
            actualArtists = validateArtist(test[INPUT]).removeDup()
            expectedArtists = test[EXPECTED_OUTPUT]
            self.assertTrue(actualArtists, expectedArtists)


if __name__ == "__main__":
    unittest.main()
