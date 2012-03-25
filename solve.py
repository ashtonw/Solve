import sys

__author__ = 'Ashton'


class Cell(object):
    flip  = False
    match = False

class Monster(Cell):
    flip  = True
    match = True

    def __init__(self, color):
        self.color = color

    def matches(self, other):
        return self.color == other.color

class Box(Cell):
    flip  = True

class CellRef(object):
    def __init__(self, board, loc):
        self.board = board
        self.cell  = board[loc]
        self.flip  = self.cell.flip
        self.match = self.cell.match


class Board(dict):
    x_max = 5
    y_max = 6

    def __init__(self):
        dict.__init__(self)

    def __init__(self, list):
        k = zip(range(0, self.x_max), range(0, self.y_max))
        dict.__init__(self, zip(k ,list))


class Game(object):
    """
    """
    def run_cycle(self, board):
        for c in board:
            pass




def main(*args):
    """ 5 x 6 max puzzle board size
    0 nullspace
    1 empty/grass
    2 box

    3 blue
    4 red etc
    """
    try:
        grid = [Monster('green'), Monster('red')]
        board = Board(grid)

    except IOError: #Exception:
        print "Oops"
    else:
        return 0

if __name__ == '__main__':
    sys.exit(main(*sys.argv))

