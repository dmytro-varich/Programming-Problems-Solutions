from piece import Piece


class Player:
    def __init__(self, color, board):
        self.color = color
        self.board = board
        self.pieces = [
            Piece(color) for _ in range(4)
        ]

    def is_done(self):
        for x in self.pieces:
            if x.position not in (40, 41, 42, 43):
                return False
        return True

    def has_active(self):
        for x in self.pieces:
            if x.position is not None:
                return True
        return False

    def get_piece_positions(self):
        lst = []
        for x in self.pieces:
            lst.append(x.position)
        return lst

    def get_valid_moves(self, roll):
        lst = []
        for n in self.pieces:
            if roll == 6 and n.active is False:
                tpl_0 = (n, 0)
                return [tpl_0]
            tpl = (n, roll)
            lst.append(tpl)
        return lst

    def prepare_targets(self, moves):
        c = 0
        for n in self.pieces:
            if n.active is False:
                c += 1
            # print(n.active)

        count = 0
        suma = 0
        for i in moves:
            for n in i:
                if isinstance(n, int):
                    if c == 4 and n == 6 and count == 0:
                        count += 1
                        n = 0
                    suma += n
                # print(suma)

        for n in self.pieces:
            # print(n.position)
            if n.position is not None:
                return [(moves[0][0], suma + n.position)]
        return list()

    def get_move(self, roll):
        # DO NOT IMPLEMENT HERE
        return list()


class RandomPlayer(Player):
    def __init__(self, color, board):
        super().__init__(color, board)

    def get_move(self, roll):
        return list()


class SafePlayer(Player):
    def __init__(self, color, board):
        super().__init__(color, board)

    def get_move(self, roll):
        return list()


class MeanPlayer(Player):
    def __init__(self, color, board):
        super().__init__(color, board)

    def get_move(self, roll):
        return list()


class EagerPlayer(Player):
    def __init__(self, color, board):
        super().__init__(color, board)

    def get_move(self, roll):
        return list()


if __name__ == '__main__':
    pass
