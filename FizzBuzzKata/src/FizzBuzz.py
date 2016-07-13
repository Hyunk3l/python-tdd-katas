
class FizzBuzz:
    FIZZ = "Fizz"
    BUZZ = "Buzz"

    def evaluate_number(self, number):
        if self.__is_fizz(number):
            return self.FIZZ
        if self.__is_buzz(number):
            return self.BUZZ
        else:
            return number

    def __is_fizz(self, number):
        return number % 3 == 0

    def __is_buzz(self, number):
        return number % 5 == 0
