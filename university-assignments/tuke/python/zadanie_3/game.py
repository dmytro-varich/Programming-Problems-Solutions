from board import Board


class Game:
    def __init__(self, player_types):
        self.board = Board()
        self.players = [
            player_types[0]('black', self.board),
            player_types[1]('yellow', self.board),
            player_types[2]('green', self.board),
            player_types[3]('red', self.board)
        ]

    def get_player_rolls(self, player):
        return list()

    def run_game(self):
        order = list()
        length = 1

        return length, order


def find_best_strategy(player_types, runs):
    return player_types[0], dict()


if __name__ == '__main__':
    pass
