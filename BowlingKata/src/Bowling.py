
class Bowling:

    STRIKE = "X"

    SPARE = "/"

    TEN_POINTS = 10

    MULTIPLE_STRIKES_SCORE = 30

    __rolls = None

    def __init__(self):
        self.__rolls = []

    def roll(self, *args):
        for score in args:
            self.__rolls.append(score)

    def get_score(self):
        total_score = 0
        for index, roll in enumerate(self.__rolls):
            if self.__is_third_strike(index):
                total_score += self.MULTIPLE_STRIKES_SCORE
            elif self.__is_strike(roll) and self.__is_next_roll_strike(index):
                continue
            elif self.__is_spare(roll):
                continue
            elif self.__is_previous_roll_spare(index):
                total_score += roll + self.TEN_POINTS
            elif self.__is_previous_roll_strike(index):
                total_score += self.TEN_POINTS + ( roll * 2 ) + self.__next_roll(index)
            elif index-1 >= 0 and self.STRIKE == self.__previous_roll(index):
                continue
            elif self.__is_strike(roll):
                continue
            else:
                total_score += roll
        return total_score

    def __next_roll(self, index):
        return self.__rolls[index + 1]

    def __is_third_strike(self, index):
        return (
            index - 2 >= 0
            and self.__two_rolls_behind(index) == self.STRIKE
            and self.__previous_roll(index) == self.STRIKE
        )

    def __is_next_roll_strike(self, index):
        return index+1 <= len(self.__rolls) and self.__next_roll(index) == self.STRIKE

    def __is_strike(self, roll):
        return self.STRIKE == roll

    def __is_spare(self, roll):
        return self.SPARE == roll

    def __is_previous_roll_spare(self, index):
        return index-1 >= 0 and self.SPARE == self.__previous_roll(index)

    def __is_previous_roll_strike(self, index):
        return index-1 >= 0 and self.STRIKE == self.__previous_roll(index)

    def __previous_roll(self, index):
        return self.__rolls[index-1]

    def __two_rolls_behind(self, index):
        return self.__rolls[index - 2]
