
class FizzBuzz:
    FIZZ = "Fizz"
    BUZZ = "Buzz"

    def evaluate_number(self, number):
        if self.__is_multiple_of_three_and_five(number):
            return self.FIZZ+self.BUZZ
        elif self.__is_multiple_of_three(number):
            return self.FIZZ
        elif self.__is_multiple_of_five(number):
            return self.BUZZ
        else:
            return number

    def __is_multiple_of_three_and_five(self, number):
        return self.__is_multiple_of_three(number) & self.__is_multiple_of_five(number)

    def __is_multiple_of_three(self, number):
        return number % 3 == 0

    def __is_multiple_of_five(self, number):
        return number % 5 == 0
