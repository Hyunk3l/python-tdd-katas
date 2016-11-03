from unittest import TestCase
from BowlingKata.src.Bowling import Bowling

class TestBowling(TestCase):

    PERFECT_SCORE = 300

    STRIKE = "X"

    STRIKE_POINTS = 10

    bowling = None

    def setUp(self):
        self.bowling = Bowling()

    def test_should_get_current_score(self):
        self.bowling.roll(self.STRIKE_POINTS)
        self.assertEqual(self.STRIKE_POINTS, self.bowling.get_score())

    def test_should_get_perfect_score(self):
        for current in range(0, 12):
            self.bowling.roll(self.STRIKE)

        self.assertEqual(self.PERFECT_SCORE, self.bowling.get_score())

    def test_should_get_score_without_strikes(self):
        # Frame 1.
        self.bowling.roll(9, 0)

        # Frame 2.
        self.bowling.roll(3, 4)

        # Frame 3.
        self.bowling.roll(1, 5)

        # Frame 4.
        self.bowling.roll(2, 2)

        # Frame 5.
        self.bowling.roll(1, 0)

        # Frame 6.
        self.bowling.roll(6, 3)

        # Frame 7.
        self.bowling.roll(0, 3)

        # Frame 8.
        self.bowling.roll(9, 0)

        # Frame 9.
        self.bowling.roll(9, 0)

        # Frame 10.
        self.bowling.roll(5, 3)

        self.assertEqual(65, self.bowling.get_score())

