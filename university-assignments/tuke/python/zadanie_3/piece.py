class Piece:
    def __init__(self, color):
        self.color = color
        self.active = False
        self.position = None

    def activate(self):
        self.active = True
        self.position = 0

    def throw_out(self):
        self.active = False
        self.position = None

    def is_done(self):
        if self.position in (40, 41, 42, 43):
            return True
        return False

    def move(self, steps):
        if self.position is None and self.active is False and steps == 6:
            return 0
        if self.position is None:
            return None
        if self.position + steps > 43:
            return self.position
        return steps + self.position

    def move_to_place(self, position):
        self.position = position
        return self.position


if __name__ == '__main__':
    pass
