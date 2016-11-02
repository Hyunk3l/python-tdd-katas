from unittest import TestCase
from BowlingKata.src.Bowling import Bowling

class TestBowling(TestCase):

    PERFECT_SCORE = 300

    STRIKE = "X"

    STRIKE_POINTS = 10

    bowling = None

    def setUp(self):
        self.bowling = Bowling()

    def test_should_get_perfect_score(self):

        for current in range(0, 12):
            self.bowling.roll(self.STRIKE)

        self.assertEqual(self.PERFECT_SCORE, self.bowling.get_score())

    def test_should_get_current_score(self):
        self.bowling.roll(self.STRIKE_POINTS)
        self.assertEqual(self.STRIKE_POINTS, self.bowling.get_score())