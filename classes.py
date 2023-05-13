class Figure:
    total_whites = 0
    total_blacks = 0
    names = ('king', 'queen', 'bishop', 'knight', 'castle', 'pawn')
    letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

    def __init__(self, position: str, name: str, color: int):
        if len(position) == 2:
            self.pos_visual = position.upper()
            self.pos_x, self.pos_y = self.__convert_position()
        else:
            self.pos_x, self.pos_y = None, None
        if color in [0, 1]:
            self.color = color
            self.color_visual = 'black' if color == 0 else 'white'
        else:
            self.color, self.color_visual = None, None
        self.name = name.lower() if name.lower() in Figure.names else None
        self.__rule = self.__get_moving_rules()

        if color == 0:
            Figure.total_blacks += 1
        else:
            Figure.total_whites += 1

        if self.pos_x is None or self.pos_y is None or self.name is None or self.color is None:
            raise Exception('ArgError')

    def __str__(self):
        return f'{self.color_visual} {self.name} stay at {self.pos_visual}'

    def __del__(self):
        print('deleted')

    def move(self, position):
        x, y = self.__convert_position(position)
        if self.__move_check(x, y):
            self.pos_x, self.pos_y, self.pos_visual = x, y, position.upper()
            return True
        else:
            return False

    def __get_moving_rules(self):
        match self.name:
            case 'king':
                return 'abs(self.pos_x - x) <= 1 and abs(self.pos_y - y) <= 1'
            case 'queen':
                return '(self.pos_x == x) or (self.pos_y == y) or (abs(self.pos_x - x) == abs(self.pos_y - y))'
            case 'bishop':
                return 'abs(self.pos_x - x) == abs(self.pos_y - y)'
            case 'knight':
                return '(abs(self.pos_x - x) == 2 and abs(self.pos_y - y) == 1) or ' \
                       '(abs(self.pos_y - y) == 2 and abs(self.pos_x - x) == 1)'
            case 'castle':
                return '(self.pos_x == x) or (self.pos_y == y)'
            case 'pawn':
                return 'self.pos_x - x == 1'

    def __move_check(self, x, y):
        if x is not None and y is not None and self.pos_x != x or self.pos_y != y:
            if not eval(self.__rule):
                return False
        else:
            return False
        return True

    def __convert_position(self, position=None):
        if position is None:
            position = self.pos_visual
        return (Figure.letters.index(position[0].lower()) if position[0].lower() in Figure.letters else None,
                int(position[1]) - 1 if position[1].isdigit() else None)


piece = Figure('a3', 'king', 1)
print(piece)
print(piece.move('b3'))
print(piece)
print(piece.move('d3'))
print(piece)
print(piece.move('c4'))
print(piece)