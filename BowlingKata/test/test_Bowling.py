
from unittest import TestCase
from BowlingKata.src.Bowling import Bowling

class TestBowling(TestCase):

    def test_should_get_current_score(self):
        bowling = Bowling()
        bowling.roll(10)
        self.assertEqual(10, bowling.getScore())

    def test_should_get_perfect_score(self):
        bowling = Bowling()
        bowling.roll(10)
        bowling.roll(10)
        bowling.roll(10)
        bowling.roll(10)
        bowling.roll(10)
        bowling.roll(10)
        bowling.roll(10)
        bowling.roll(10)
        bowling.roll(10)
        bowling.roll(10)
        self.assertEquals(300, bowling.getScore())