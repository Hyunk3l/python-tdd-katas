
class Bowling:

    STRIKE = "X"

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
            elif self.STRIKE == roll and self.__is_next_roll_strike(index):
                continue
            else:
                total_score += roll
        return total_score

    def __is_third_strike(self, index):
        return (
            index - 2 >= 0
            and self.__rolls[index-2] == self.STRIKE
            and self.__rolls[index-1] == self.STRIKE
        )

    def __is_next_roll_strike(self, index):
        return index+1 <= len(self.__rolls) and self.__rolls[index+1] == self.STRIKE