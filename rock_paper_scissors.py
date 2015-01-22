__author__ = 'Saqib Razaq'

from random import choice as randchoice
from time import sleep

"""
Simple implementation of Rock Paper Scissors in Python
"""

players = "XY"
ai_players = "Y"
moves = ['r', 'p', 's']
wins = ("rp", "sr", "ps")
status = "%5s %3d %5s %3d   moves: %s %s"
pause_time = 0.3


class RockPaperScissors(object):

    def run(self):
        scores = [0, 0]

        while True:
            choice1, choice2 = (self.get_move(p) for p in players)

            if choice1 != choice2:
                winner = 1 if (choice1+choice2 in wins) else 0
                scores[winner] += 1

            print(status % (players[0], scores[0], players[1], scores[1], choice1, choice2))
            sleep(pause_time)

    def get_move(self, player):
        if player in ai_players:
            return randchoice(moves)
        else:
            return self.get_input()

    def get_input(self):
        text_input = ''
        while text_input not in moves:
            text_input = raw_input('Please enter (r|p|s):')
        return text_input


if __name__ == '__main__':
        RockPaperScissors().run()
