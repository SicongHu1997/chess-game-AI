from copy import deepcopy
from random import shuffle

def eliminate(board, colour):
    if colour == "black":
        for row in range(0,8):
            for column in range(0,8):
                if board[row][column]=="O":
                    if row!=0 and row!=7:
                        if (board[row+1][column]=="@" or board[row+1][column]=="X") and (board[row-1][column]=="@" or board[row-1][column]=="X"):
                            board[row][column] = "-"
                    if column!=0 and column!=7:
                        if (board[row][column+1]=="@" or board[row][column+1]=="X") and (board[row][column-1]=="@" or board[row][column-1]=="X"):
                            board[row][column] = "-"
        for row in range(0,8):
            for column in range(0,8):
                if board[row][column]=="@":
                    if row!=0 and row!=7:
                        if (board[row+1][column]=="O" or board[row+1][column]=="X") and (board[row-1][column]=="O" or board[row-1][column]=="X"):
                            board[row][column] = "-"
                    if column!=0 and column!=7:
                        if (board[row][column+1]=="O" or board[row][column+1]=="X") and (board[row][column-1]=="O" or board[row][column-1]=="X"):
                            board[row][column] = "-"
    if colour == "white":
        for row in range(0,8):
            for column in range(0,8):
                if board[row][column]=="@":
                    if row!=0 and row!=7:
                        if (board[row+1][column]=="O" or board[row+1][column]=="X") and (board[row-1][column]=="O" or board[row-1][column]=="X"):
                            board[row][column] = "-"
                    if column!=0 and column!=7:
                        if (board[row][column+1]=="O" or board[row][column+1]=="X") and (board[row][column-1]=="O" or board[row][column-1]=="X"):
                            board[row][column] = "-"
        for row in range(0,8):
            for column in range(0,8):
                if board[row][column]=="O":
                    if row!=0 and row!=7:
                        if (board[row+1][column]=="@" or board[row+1][column]=="X") and (board[row-1][column]=="@" or board[row-1][column]=="X"):
                            board[row][column] = "-"
                    if column!=0 and column!=7:
                        if (board[row][column+1]=="@" or board[row][column+1]=="X") and (board[row][column-1]=="@" or board[row][column-1]=="X"):
                            board[row][column] = "-"
    return None
# def eliminate(board, colour):
#
#     remove(board, colour)
#     colour = opposite(colour)
#     remove(board, colour)
#     return None
# def remove(board, colour):
#     colour = symbol(colour)
#     reverse_colour = reverse(colour)
#     for row in range(0,8):
#         for column in range(0,8):
#             if board[row][column] == reverse_colour:
#                 if row!=0 and row!=7:
#                     if (board[row+1][column]==colour or board[row+1][column]=="X") and (board[row-1][column]==colour or board[row-1][column]=="X"):
#                         board[row][column] = "-"
#                 if column!=0 and column!=7:
#                     if (board[row][column+1]==colour or board[row][column+1]=="X") and (board[row][column-1]==colour or board[row][column-1]=="X"):
#                         board[row][column] = "-"
def shrink(board, turns):
    if turns >= 128 and turns < 192:
        for x in range(8):
            board[0][x] = ' '
            board[7][x] = ' '
            board[x][0] = ' '
            board[x][7] = ' '
        for square in [(1, 1), (6, 1), (6, 6), (1, 6)]:
            i, j = square
            board[j][i] = 'X'

    if turns >= 192:
        for x in range(8):
            board[1][x] = ' '
            board[6][x] = ' '
            board[x][1] = ' '
            board[x][6] = ' '
            board[0][x] = ' '
            board[7][x] = ' '
            board[x][0] = ' '
            board[x][7] = ' '
        for square in [(2, 2), (5, 2), (2, 5), (5, 5)]:
            i, j = square
            board[j][i] = 'X'

def symbol(colour):
    return "@" if colour == 'black' else "O"
# def reverse(colour):
#     return "O" if colour == 'black' else "@"
def opposite(colour):
    return 'white' if colour == 'black' else 'black'

def tp_to_board(tp, turns):
    board = [['-' for _ in range(8)] for _ in range(8)]
    for square in [(0, 0), (7, 0), (7, 7), (0, 7)]:
        x, y = square
        board[y][x] = 'X'
    for piece in tp[0]:
        board[piece[1]][piece[0]]="O"
    for piece in tp[1]:
        board[piece[1]][piece[0]]="@"
    shrink(board, turns)

    return board

def board_to_tp(board):
    tp = [[],[]]
    for row in range(0,8):
        for column in range(0,8):
            if board[row][column]=="O":
                tp[0].append((column,row))
            if board[row][column]=="@":
                tp[1].append((column,row))
    return (tuple(tp[0]),tuple(tp[1]))


def score_placing(board, colour):
    score = 0
    if colour == 'white':
        for row in range(0,8):
            for column in range(0,8):
                if board[row][column]=="O":
                    score += 110;
                    score += (min(row,(7-row)))*(min(column,(7-column)))
                    # if column == 5:
                    #     score -= 10
                    # if column == 4:
                    #     score += 10
                if board[row][column]=="@":
                    score -= 100;
                    score -= (min(row,(7-row)))*(min(column,(7-column)))
    else:
        for row in range(0,8):
            for column in range(0,8):
                if board[row][column]=="@":
                    score += 110;
                    score += (min(row,(7-row)))*(min(column,(7-column)))
                    # if column == 2:
                    #     score -= 10
                    # if column == 3:
                    #     score += 10
                if board[row][column]=="O":
                    score -= 100;
                    score -= (min(row,(7-row)))*(min(column,(7-column)))
    return score

def update_board(board, space, colour):
    x, y = space
    if colour == 'white':
        board[y][x] = 'O'
    else:
        board[y][x] = '@'
    return board


def empty(board, colour):
    empty = []
    rand_white_col = list(range(8))
    # shuffle(rand_white_col)
    rand_white_row = list(range(6))
    # shuffle(rand_white_row)
    rand_black_row = list(range(2,7))
    # shuffle(rand_black_row)
    if colour == 'white':
        for x in rand_white_col:
            for y in rand_white_row:
                if board[y][x] == '-':
                    space = (x,y)
                    empty.append(space)
    if colour == 'black':
        for x in rand_white_col:
            for y in rand_black_row:
                if board[y][x] == '-':
                    space = (x,y)
                    empty.append(space)
    return empty

def surround_empty(board, colour):
    """only return those squares around the current pieces"""
    whitep = pieces(board, "white")
    blackp = pieces(board, "black")
    """use these coordinates to find surrounding squres"""
    white_empty = surround(board, whitep)
    # print("white:")
    # print(white_empty)
    black_empty = surround(board, blackp)
    # print("black:")
    # print(black_empty)
    merged_empty = merge_empty(white_empty,black_empty)
    # print("merged:")
    # print(merged_empty)
    empty = []
    for piece in merged_empty:
        x, y = piece
        if within_colour(colour, x, y):
            empty.append(piece)

    # print("after:")
    # print(empty)
    return empty

def within_colour(colour, x, y):
    if colour == "white":
        if y < 6:
            return True
        else:
            return False
    if colour == "black":
        if y > 2:
            return True
        else:
            return False

def surround(board, pieces):
    empty =[]
    ks = ()
    adj = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
    adj_2 = []
    adj_3 = [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(2,-1),(-2,-1),(-2,-1)]
    # for a in adj:
    #     i, j = a
    #     i = i*2
    #     j = j*2
    #     new_a = (i,j)
    #     adj_2.append(new_a)
    # adj = adj + adj_2 +adj_3
    # print(adj)
    for piece in pieces:
        x, y = piece
        for ks in adj:
            dx, dy = ks
            # print(dx, dy)
            x_new = x + dx
            y_new = y + dy
            # print(x,y)
            if is_empty(board, x_new, y_new):
                p = (x_new,y_new)
                empty.append(p)
    return empty

def merge_empty(white_empty, black_empty):
    all_empty = white_empty + black_empty
    empty = []
    for s in all_empty:
        if s not in empty:
            empty.append(s)

    return empty

def is_empty(board, x, y):
    if x in range(8) and y in range(8):
        if board[y][x] == '-':
            return True
    return False

def pieces(board, colour):
    pieces = []
    rand = list(range(8))
    shuffle(rand)

    for x in rand:
        for y in rand:
            if board[y][x] == 'O' and colour == 'white':
                piece = (x, y)
                pieces.append(piece)
            if board[y][x] == '@' and colour == 'black':
                piece = (x, y)
                pieces.append(piece)
    return pieces

def moves(board, colour, piece, turns):
    move = []
    x, y = piece
    dir = [(0,1), (0,-1), (1,0), (-1,0)]
    for i in dir:
        dx, dy = i
        nx = x + dx
        ny = y + dy
        new_piece = (nx, ny)
        if within_board(new_piece, turns):
            if board[ny][nx] == '-':
                move.append(new_piece)
            else:
                if board[ny][nx] == '@' or board[ny][nx] == 'O':
                    nnx = x + dx + dx
                    nny = y + dy + dy
                    next_piece = (nnx,nny)
                    if within_board(next_piece, turns):
                        if board[nny][nnx] == '-':
                            move.append(next_piece)
    return move
# return a updated tupple board
def update_move(board, colour, from_piece, to_piece):
    curr_board = deepcopy(board)
    x,y = from_piece
    x1,y1 = to_piece
    my_symbol = symbol(colour)
    curr_board[y][x] = '-'
    curr_board[y1][x1] = my_symbol
    eliminate(curr_board, colour)
    curr_board = board_to_tp(curr_board)
    return curr_board

def within_board(piece, turns):
    x, y = piece
    if turns >= 192:
        max = 6
        min = 2
    if turns >= 128 and turns <192:
        max = 7
        min = 1
    if turns < 128:
        max = 8
        min = 0
    if x < max and x >= min and y < max and y >= min:
        return True
    else:
        return False

class Player:
    # initialise the board and change the representation of the board
    def __init__(self, colour):
        # set up my colour and opponent's colour
        self.colour = colour
        # set up my valid board and enemy's valid board for placing
        # using a Board Object
        self.board = [['-' for _ in range(8)] for _ in range(8)]
        for square in [(0, 0), (7, 0), (7, 7), (0, 7)]:
            x, y = square
            self.board[y][x] = 'X'
        # turns counter
        self.turns = 0
        self.state = "placing"
    def update(self, action):
        self.turns += 1
    #    print(self.turns)
        if self._is_Placing():
            if self.colour=="white":
                self.board[action[1]][action[0]] = "@"
            else:
                self.board[action[1]][action[0]] = "O"
        else:
            self.board[action[0][1]][action[0][0]] = "-"
            if self.colour=="white":
                self.board[action[1][1]][action[1][0]] = "@"
            else:
                self.board[action[1][1]][action[1][0]] = "O"
        shrink(self.board, self.turns)
        eliminate(self.board, opposite(self.colour))
    #    print("print by update")
    #    for row in range(0,8):
    #        print(self.board[row][0]+" "+self.board[row][1]+" "+self.board[row][2]+" "+self.board[row][3]
    #              +" "+self.board[row][4]+" "+self.board[row][5]+" "+self.board[row][6]+" "+self.board[row][7])
    def action(self, turns):
        self.turns += 1
    #    print(self.turns)
        if self._is_Placing():
            if self.turns == 1:
                move = (3,3)
                update_board(self.board, move, self.colour)
                return move
            if self.turns == 2:
                dir = [(0,1),(0,-1),(1,0),(-1,0),(0,0)]
                move = (4,4)
                x, y = move
                for i in dir:
                    dx, dy = i
                    new_x = x + dx
                    new_y = y + dy
                    if is_empty(self.board, new_x, new_y) is False:
                        board = board_to_tp(self.board)
                        root = Tree(None, board, opposite(self.colour), 0, None)
                        ab = Alphabeta(root, turns)
                        best_state = ab.alpha_beta_search(root)
                        move = best_state.move
                        update_board(self.board, move, self.colour)
                        return move
                update_board(self.board, move, self.colour)
                return move
            board = board_to_tp(self.board)
            root = Tree(None, board, opposite(self.colour), 0, None)
            ab = Alphabeta(root, turns)
            best_state = ab.alpha_beta_search(root)
            move = best_state.move
            update_board(self.board, move, self.colour)

            new_board = tp_to_board(board, turns)
        else:
            # playing phase return 2 tuples, from (a,b) to (c,d)
            board = board_to_tp(self.board)
            root = Tree(None, board, self.colour, 0, None)
            ab = Alphabeta_play(root, turns)
            print(turns)
            best_state = ab.alpha_beta_search(root)
            move = best_state.move
            from_piece = move[0]
            to_piece =move[1]

            self.board = tp_to_board(update_move(self.board,self.colour,from_piece, to_piece), turns)
        eliminate(self.board, self.colour)
        #    a, b, c, d = map(int, input().split())
        #    self.board[b][a] = "-"
        #    if self.colour=="white":
        #        self.board[d][c] = "O"
        #    else:
        #        self.board[d][c] = "@"
        #    move = ((a,b),(c,d))

        print("print by action")
        for row in range(0,8):
            print(self.board[row][0]+" "+self.board[row][1]+" "+self.board[row][2]+" "+self.board[row][3]
                  +" "+self.board[row][4]+" "+self.board[row][5]+" "+self.board[row][6]+" "+self.board[row][7])

        return move
    def _is_Placing(self):
        if self.state == "placing" and self.turns == 25:
            self.state = "playing"
            self.turns = 0

        if self.state =="placing":
            return True
        if self.state == "playing":
            return False
        return None

class Alphabeta_play:

    def __init__(self, root, turns):
        self.root = root
        self.turns = turns

    def alpha_beta_search(self, node):
        infinity = float('inf')
        alpha = -infinity
        beta = infinity
        board = tp_to_board(node.board, self.turns)
        eliminate(board, node.colour)


        # current active pieces
        successors = pieces(board, node.colour)
        print(successors)
        best_state = None
        for from_piece in successors:
            # find all possible moves
            # print(self.turns)
            all_moves = moves(board, node.colour, from_piece, self.turns)
            print(all_moves)
            for to_piece in all_moves:

                new_board = update_move(board, node.colour, from_piece, to_piece)
                colour = opposite(node.colour)
                move = (from_piece, to_piece)

                state = Tree(None, new_board, colour, 1, move)
                node.add_child(state)
                value = self.min_value(state, alpha, beta)
                if value > alpha:
                    alpha = value
                    best_state = state
        if best_state == None:
            best_state = state
        return best_state

    def max_value(self, node, alpha, beta):
        if self.isTerminal(node):
            return self.getValue(node)
        infinity = float('inf')
        value = -infinity

        current_turns = self.turns + node.level
        board = tp_to_board(node.board, current_turns)
        colour = node.colour
        eliminate(board, colour)

        successors = pieces(board, colour)
        # if successors is None:
        #     return self.getValue(node)
        for from_piece in successors:
            # board = tp_to_board(node.board, current_turns)
            all_moves = moves(board, node.colour, from_piece, current_turns)
            # if all_moves is None:
            #     return self.getValue(node)
            for to_piece in all_moves:
                #board to tp
                new_board = update_move(board, colour, from_piece, to_piece)
                colour = opposite(colour)
                level = node.level + 1
                move = (from_piece, to_piece)

                state = Tree(None, new_board, colour, level, move)
                node.add_child(state)

                value = max(value, self.min_value(state, alpha, beta))
                if value >= beta:
                    return value
                alpha = max(alpha, value)
        return value

    def min_value(self, node, alpha, beta):
        if self.isTerminal(node):
            return self.getValue(node)
        infinity = float('inf')
        value = infinity

        current_turns = self.turns + node.level
        board = tp_to_board(node.board, current_turns)
        colour = node.colour
        eliminate(board, colour)

        successors = pieces(board, colour)

        for from_piece in successors:
            all_moves = moves(board, node.colour, from_piece, current_turns)
            # if all_moves is None:
            #     return self.getValue(node)
            for to_piece in all_moves:
                # board to tupple
                new_board = update_move(board, colour, from_piece, to_piece)
                colour = opposite(colour)
                level  = node.level + 1
                move = (from_piece, to_piece)
                state = Tree(None, new_board, colour, level, move)
                node.add_child(state)

                value = min(value, self.max_value(state, alpha, beta))
                if value <= alpha:
                    return value
                beta = min(beta, value)
        return value

    def getValue(self, node):
        assert node is not None
        return score_placing(tp_to_board(node.board, self.turns), self.root.colour)

    def isTerminal(self, node):
        assert node is not None

        if self.turns <=128:
             level = 3
        else:
            if self.turns <=192:
             level = 4
            else:
                level = 5
        return node.level == level
# alphabeta pruning
class Alphabeta:

    def __init__(self, root, turns):
        self.root = root
        self.turns = turns

    def alpha_beta_search(self, node):
        infinity = float('inf')
        alpha = -infinity
        beta = infinity

        # successors = empty(tp_to_board(node.board), opposite(node.colour))
        # if self.turns < 24:
        successors = surround_empty(tp_to_board(node.board, self.turns), opposite(node.colour))

        # print(successors)
        best_state = None
        for spaces in successors:
            # add peice to board
            # tp to board, board to tp, create child node
            board = tp_to_board(node.board, self.turns)
            colour = opposite(node.colour)
            board = update_board(board, spaces, colour)
            eliminate(board, colour)
            board = board_to_tp(board)

            state = Tree(None, board, colour, 1, spaces)
            node.add_child(state)
            value = self.min_value(state, alpha, beta)
            if value > alpha:
                alpha = value
                best_state = state
        return best_state


    def max_value(self, node, alpha, beta):
        if self.isTerminal(node):
            return self.getValue(node)
        infinity = float('inf')
        value = -infinity

        # successor = self.createSuccessors(node)
        # if self.turns < 24:
        successor = surround_empty(tp_to_board(node.board, self.turns), opposite(node.colour))
        for spaces in successor:
            #add_to_board(node.self.board, )
            board = tp_to_board(node.board, self.turns)
            colour = opposite(node.colour)
            board = update_board(board, spaces, colour)
            eliminate(board, colour)
            board = board_to_tp(board)
            level = node.level
            level += 1
            state = Tree(None, board, colour, level, spaces)
            node.add_child(state)

            value = max(value, self.min_value(state, alpha, beta))
            if value >= beta:
                return value
            alpha = max(alpha, value)

        return value

    def min_value(self, node, alpha, beta):
        # if this is the 4th level, then calculate heuristic value
        if self.isTerminal(node):
            # need to use heuristic function to calculate value
            return self.getValue(node)
        infinity = float('inf')
        value = infinity

        # successor = self.createSuccessors(node)
        successor = surround_empty(tp_to_board(node.board, self.turns), opposite(node.colour))
        for spaces in successor:
            #add_to_board(node.self.board, )
            colour = opposite(node.colour)
            board = tp_to_board(node.board, self.turns)
            board = update_board(board, spaces, colour)
            eliminate(board, colour)
            board = board_to_tp(board)
            level = node.level
            level += 1
            state = Tree(None, board, colour, level, spaces)
            node.add_child(state)
            value = min(value, self.max_value(state, alpha, beta))
            if value <= alpha:
                return value
            beta = min(beta, value)

        return value

    def getSuccessors(self, node):
        assert node is not None
        return node.children

    def createSuccessors(self, node):
        board = tp_to_board(node.board)
        return empty(board,opposite(node.colour))

    def isTerminal(self, node):
        assert node is not None

        # if self.turns < 10:
        #     level = 4
        # else:
        #     level = 4
        level = 4
        return node.level == level

    def getValue(self, node):
        assert node is not None
        return score_placing(tp_to_board(node.board,self.turns), opposite(self.root.colour))


# The basic structure of a tree
class Tree:
    def __init__(self, value, tuple_board, colour, level, move):
        self.value = value
        self.children = []
        self.board = tuple_board
        self.colour = colour
        self.level = level
        self.move = move
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)
