import unittest
from guess import game


class TestGuess(unittest.TestCase):
    def setUp(self):
        print("ready to test function.")

    def test_input(self):
        result = game(5, 5)
        self.assertTrue(result)

    def test_wrong_guess(self):
        result = game(5, 9)
        self.assertFalse(result)

    def test_wrong_input(self):
        result = game(5, 11)
        self.assertFalse(result)

    def test_wrong_type(self):
        result = game(5, "11")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
