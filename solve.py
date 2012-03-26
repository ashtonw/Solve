import sys

__author__ = 'Ashton'


class Cell(object):
    flip  = False
    match = False

    def __init__(self, board=None, loc=None):
        self.board = board
        self.loc   = loc

    def getAdjacent(self, d):
        x,y = self.loc
        if d   == 'N' or d == 0:
            y += 1
        elif d == 'E' or d == 1:
            x += 1
        elif d == 'S' or d == 2:
            y -= 1
        elif d == 'W' or d == 3:
            x -= 1
        elif d >= 4:
            raise IndexError
        return self.board[(x,y)]

    def adjacent(self):
        """generator for the adjacent cells"""
        d = 0
        while d < 4:
            a = self.getAdjacent(d)
            if a is not None:
                yield a
            d += 1


    def getAbove(self):
        return self.getAdjacent('N')
    def getBelow(self):
        return self.getAdjacent('S')
    def getLeft(self):
        return self.getAdjacent('W')
    def getRight(self):
        return self.getAdjacent('E')

class Monster(Cell):
    flip  = True
    match = True

    def __init__(self, color):
        Cell.__init__(self)
        self.color = color

    def matches(self, other):
        return self.color == other.color

class Box(Cell):
    flip  = True


class Board(dict):
    x_max = 5
    y_max = 6

    def __init__(self):
        dict.__init__(self)

    def __init__(self, list):
        k = [[0 for i in range(self.x_max)] for j in range(self.y_max)]
        dict.__init__(self)
        for loc,cell in zip(k ,list):
            self[tuple(loc)] = cell

    def __setitem__(self, loc, cell):
        cell.loc = loc
        cell.board = self
        super(Board,self).__setitem__(loc,cell)

    def __repr__(self):
        k = [[0 for i in range(self.x_max)] for j in range(self.y_max)]
        repr = [i.__repr__() for i in k]
        return '\n'.join(repr)



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

        print board
    except IOError: #Exception:
        print "Oops"
    else:
        return 0

if __name__ == '__main__':
    sys.exit(main(*sys.argv))

