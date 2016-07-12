from unittest import TestCase
from FizzBuzzKata.src.FizzBuzz import FizzBuzz


class TestFizzBuzz(TestCase):

    FIZZ = "Fizz"

    BUZZ = "Buzz"

    __fizz_buzz = None

    def setUp(self):
        self.__fizz_buzz = FizzBuzz()

    def test_should_print_fizz_on_multiples_of_three(self):
        output = self.__fizz_buzz.evaluate_number(3)
        self.assertEqual(self.FIZZ, output)

    def test_should_print_buzz_on_multiples_of_five(self):
        output = self.__fizz_buzz.evaluate_number(5)
        self.assertEqual(self.BUZZ, output)
