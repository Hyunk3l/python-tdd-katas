
class FizzBuzz:
    FIZZ = "Fizz"
    BUZZ = "Buzz"

    def evaluate_number(self, number):
        if self.__is_multiple_of_three_and_five(number):
            return self.FIZZ + self.BUZZ
        elif self.__is_fuzzable(number):
            return self.FIZZ
        elif self.__is_buzzable(number):
            return self.BUZZ
        else:
            return number

    def __is_fuzzable(self, number):
        return self.__is_multiple_of_three(number) | self.__has_number_a_three(number)

    def __is_buzzable(self, number):
        return self.__is_multiple_of_five(number) | self.__has_number_a_five(number)

    def __is_multiple_of_three_and_five(self, number):
        return self.__is_multiple_of_three(number) & self.__is_multiple_of_five(number)

    def __is_multiple_of_three(self, number):
        return number % 3 == 0

    def __is_multiple_of_five(self, number):
        return number % 5 == 0

    def __has_number_a_three(self, number):
        return 0 <= str(number).find(str(3))

    def __has_number_a_five(self, number):
        return 0 <= str(number).find(str(5))
