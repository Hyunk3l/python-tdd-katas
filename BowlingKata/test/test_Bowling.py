from unittest import TestCase
from BowlingKata.src.Bowling import Bowling


class TestBowling(TestCase):

    bowling = None

    def setUp(self):
        self.bowling = Bowling()

    def test_should_get_perfect_score(self):

        self.bowling.roll("X")
        self.bowling.roll("X")
        self.bowling.roll("X")
        self.bowling.roll("X")
        self.bowling.roll("X")
        self.bowling.roll("X")
        self.bowling.roll("X")
        self.bowling.roll("X")
        self.bowling.roll("X")
        self.bowling.roll("X")
        self.bowling.roll("X")
        self.bowling.roll("X")

        self.assertEqual(300, self.bowling.getScore())

    def test_should_get_current_score(self):
        self.bowling.roll(10)
        self.assertEqual(10, self.bowling.getScore())