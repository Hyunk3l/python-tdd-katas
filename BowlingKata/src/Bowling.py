
class Bowling:

    __rolls = []

    def roll(self, score):
        self.__rolls.append(score)

    def getScore(self):
        totalScore = 0
        for roll in self.__rolls:
            totalScore += roll
        return totalScore