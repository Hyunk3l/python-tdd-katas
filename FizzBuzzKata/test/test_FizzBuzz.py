from unittest import TestCase
from FizzBuzzKata.src.FizzBuzz import FizzBuzz


class TestFizzBuzz(TestCase):

    def test_should_print_fizz_on_multiples_of_three(self):
        fizz_buzz = FizzBuzz()

        output = fizz_buzz.evaluate_number(3)
        expected_output = "Fizz"
        self.assertEqual(expected_output, output)

    def test_should_print_buzz_on_multiples_of_five(self):
        fizz_buzz = FizzBuzz()

        output = fizz_buzz.evaluate_number(5)
        expected_output = "Buzz"
        self.assertEqual(expected_output, output)
