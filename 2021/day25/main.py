import copy


def width(board):
    return len(board[0])

def height(board):
    return len(board)

def print_board(board):
    print(width(board), 'x', height(board))
    for row in board:
        for col in row:
            print(col, end='')
        print()

def right(board, x,y):
    x = x + 1
    if x > width(board) - 1:
        x = 0
    return (x, y)

def down(board, x,y):
    y = y + 1
    if y > height(board) - 1:
        y = 0
    return (x, y)

def move(board):
    newboard = copy.deepcopy(board)
    # rightwards
    for y, row in enumerate(board):
        for x, ch in enumerate(row):
            if ch == '>':
                r = right(board, x, y)
                if board[y][r[0]] == '.':
                    newboard[y][x] = '.'
                    newboard[y][r[0]] = '>'
    # downwards
    for y, row in list(reversed(list(enumerate(board)))):
            for x, ch in enumerate(row):
                if ch == 'v':
                    r = down(board, x, y)
                    if board[r[1]][x] != 'v' and newboard[r[1]][x] != '>':
                        newboard[y][x] = '.'
                        newboard[r[1]][x] = 'v'
    return newboard
        
def compare(b, nb):
    for y, row in enumerate(b):
        for x, ch in enumerate(row):
            if nb[y][x] != ch:
                return False
    return True





def cucumber():
  inp = open('input.txt', 'r')
  board = []
  for line in inp.readlines():
    row = []
    for char in line.strip():
        row.append(char)
    board.append(row)

  same = False
  iters = 0
  while not same:
    #print_board(board)
    nb = move(board)
    same = compare(nb, board)
    board = nb
    iters = iters + 1
    print(iters)
  print(iters)
  


if __name__ == '__main__':
    cucumber()

