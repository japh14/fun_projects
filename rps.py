"""
Rock, Paper, Scissors Game!!

"""

from random import randint


class Player:
    options = ("ROCK", "PAPER", "SCISSORS")
    letter_options = (options[0][0], options[1][0], options[2][0])

    def __init__(self, player_name="Computer", player_type_indicator=0):
        self.player_name = player_name
        self.player_type_indicator = player_type_indicator
        self.player_type = "computer" if player_type_indicator == 0 else "human"
        self.player_choose = None
        self.player_letter_choose = None
        self.current_shoot = None
        self.current_shoot_letter = None

    def __repr__(self):
        return f'<Player:{self.name}, Type:{self.type}>'

    @property
    def name(self):
        return self.player_name

    @property
    def type(self):
        return self.player_type

    @classmethod
    def computer_shoot(cls):
        cls.begin = True
        return cls.options[randint(0, 2)]

    def shoot(self, play=None):
        if self.player_type_indicator == 0:
            self.current_shoot = self.computer_shoot()
            self.current_shoot_letter = self.current_shoot[0]
            return self.current_shoot
        else:
            self.player_choose = str(play).upper().strip()
            i = self.letter_options.index(self.player_choose[0])
            self.player_choose = self.options[i]
            if self.player_choose[0] not in self.letter_options or self.player_choose not in self.options:
                return None
            else:
                self.current_shoot = self.player_choose
                self.current_shoot_letter = self.player_choose[0]
                return self.current_shoot


def who_won(player1, player2):
    winning_combinations = [
        ("RP", "P", player2),
        ("PR", "P", player1),
        ("PS", "S", player2),
        ("SP", "S", player1),
        ("RS", "R", player1),
        ("SR", "R", player2)
    ]

    if player1.current_shoot_letter == player2.current_shoot_letter: return None

    current_combination = player1.current_shoot_letter + player2.current_shoot_letter

    for winner_combination, _, a_winner in winning_combinations:
        if current_combination == winner_combination:
            return a_winner


if __name__ == "__main__":

    no_winner = False

    player1_name = input('Enter player name: ')
    p1 = Player(player_name=player1_name, player_type_indicator=1)
    p2 = Player(player_name="Bot1", player_type_indicator=0)

    while not no_winner:
        player_choose = input(f'{p1.name}, ROCK, PAPER, SCISSORS? ')
        p1.shoot(player_choose)
        p2.shoot()

        print(f'{p1.name}:{p1.current_shoot}   vs   {p2.name}:{p2.current_shoot}')

        winner = who_won(p1, p2)
        if isinstance(winner, Player) or winner:
            print(f'The winner is {winner.name}!!')
            no_winner = True
        else:
            print(f'No Winner :-(\n')
            pass
