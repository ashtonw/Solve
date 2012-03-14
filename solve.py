from collections import defaultdict
import sys

__author__ = 'Ashton'

class Puzzle(object):

    def __init__(self):
        self.board = defaultdict(char)

def main(*args):
    try:
        print "done"
    except Exception:
        print "Oops"
    else:
        return 0

if __name__ == '__main__':
    sys.exit(main(*sys.argv))

