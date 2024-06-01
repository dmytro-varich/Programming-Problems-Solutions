from piece import Piece
from player import Player

STARTING_POSITIONS = {
    'black': 0,
    'yellow': 10,
    'green': 20,
    'red': 30
}


class Board:
    def __init__(self):
        self.board = [None for _ in range(40)]

    def normalize_position(self, position, player_color):
        if position is None:
            return None
        if STARTING_POSITIONS[player_color] + position < 40:
            return STARTING_POSITIONS[player_color] + position
        return STARTING_POSITIONS[player_color] + position - 40

    def can_move_there(self, player, piece, position):
        for i in player.pieces:
            if i.position == position:
                return False
        return True

    def process_player_moves(self, player, targets):

        color = ' '
        for i in player.pieces:
            print(f'{i.position}, {i.color}')
            if targets[0][0] == i:
                color = i.color
        print(targets[0][0], ' ', targets[0][1])

        pos_norm = self.normalize_position(targets[0][1], color)
        for i in player.pieces:
            if targets[0][0] == i:
                i.position = targets[0][1]

        for element in self.board:
            print(element)

        

if __name__ == '__main__':
    pass
