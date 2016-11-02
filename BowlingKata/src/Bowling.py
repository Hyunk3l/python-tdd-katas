
class Bowling:

    __rolls = None

    def __init__(self):
        self.__rolls = []

    def roll(self, score):
        self.__rolls.append(score)

    def getScore(self):
        totalScore = 0
        for index, roll in enumerate(self.__rolls):
            if index - 2 >= 0 and self.__rolls[index-2] == "X" and self.__rolls[index-1] == "X":
                totalScore += 30
            elif "X" == roll and index+1 <= len(self.__rolls) and self.__rolls[index+1] == "X":
                continue
            else:
                totalScore += roll
        return totalScore