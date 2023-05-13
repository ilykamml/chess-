class Figure:
    total_whites = 0
    total_blacks = 0
    names = ('king', 'queen', 'bishop', 'knight', 'rook', 'castle', 'pawn')
    letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

    def __init__(self, pos_char: str, pos_digit: int, name: str, color: int):
        self.pos_c = pos_char.upper() if pos_char.lower() in Figure.letters else None
        self.pos_d = pos_digit if 0 < pos_digit < 9 else None
        self.name = name.lower() if name.lower() in Figure.names else None
        self.color = 'black' if color == 0 else 'white' if color == 1 else None

        if color == 0:
            Figure.total_blacks += 1
        else:
            Figure.total_whites += 1

        if self.pos_c is None or self.pos_d is None or self.name is None or self.color is None:
            raise Exception('ArgError')

    def __str__(self):
        return f'{self.color} {self.name} stay at {self.pos_c}{self.pos_d}'

    def __del__(self):
        print('deleted')

    def __move(self, pos_c: str, pos_d: int):
        if pos_c.lower() in Figure.letters and 0 < pos_d < 9:
            self.pos_c = pos_c.upper()
            self.pos_d = pos_d
        else:
            return 0
        return 1


piece = Figure('a', 3, 'king', 2)
print(piece)