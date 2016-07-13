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

    def test_should_print_number_on_non_multiple_of_five_or_three(self):
        non_multiple_of_five_or_three = 11
        output = self.__fizz_buzz.evaluate_number(non_multiple_of_five_or_three)
        self.assertEqual(non_multiple_of_five_or_three, output)

    def test_should_print_fizzbuzz_when_multiple_of_three_and_five(self):
        output = self.__fizz_buzz.evaluate_number(15)
        self.assertEqual(self.FIZZ+self.BUZZ, output)