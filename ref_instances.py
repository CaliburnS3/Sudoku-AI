import search
import random
import sys, traceback


# A trivial Problem definition
class LightSwitch(search.Problem):
    # initial state constructor inherited

    def actions(self, state):
        return ['up', 'down']

    def result(self, state, action):
        if action == 'up':
            return 'on'
        else:
            return 'off'

    def goal_test(self, state):
        return state == 'on'


switch = LightSwitch('off')
switch.label = 'Light Switch'


class FloodGame(search.Problem):

    def __init__(self, initial=None, moves=10000):

        #self.Flood = [[0, 0], ]
        fColor = 'G'  # flood color always starts as Green
        # acts as oldColor
        #self.goal = goal
        self.initial = initial
        self.state = self.initial
        #for r in range(len(self.state)):
        #    for c in range(len(self.state[0])):
        #        print(self.state[r][c])



        # print(self.result(self.fcolor, "R"))

    def actions(self, state):  # Actions should be complete for now.
        actions = ['R', 'G', 'B', 'Y', 'O', 'P']
        # get the current color of the flood and takes it away from the actions available list
        actions.remove(state[0][0])
        # if any(self.state != s for s in actions):
        return actions

    def result(self, state, action):
        #board = [[c for c in row]
        #              for row in self.initial]
        #change self.board to self.Flood so we only iterate over our current flood.
        #neighbors = getNeighbors()
        flood, borders = self.initalNeighbors(0, 0, state, action)
        for r in range(len(state)):
            for c in range(len(state[0])):
                #neighborColor will return a list of neighbors to check?
                flood, borders = self.getNeighbors(r, c, state, action, flood, borders)
                #flood = recall[0]
                #borders = recall[1]
                #remove flood references
                #if self.Flood[r][c] == self.fColor:
                #    self.Flood[r][c] = action
        board = [[c for c in row]
                 for row in state]
        for n in flood:
            n = action
        for m in borders:
            board[m[0]][m[1]] = action
        newState = tuple([''.join(row)
                          for row in board])
        return newState

    def goal_test(self, state):  # should work for any color now
        board = [[c for c in row]
                      for row in self.initial]
        total = len(board) * len(board[0])
        count = 0
        fColor = board[0][0]
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != fColor:
                    return False
        return True

    def getBorders(self, state):
        #lost forest for the trees, why do we want borders?
        # maybe need a 2D array to return the posiiton as well
        # key issue is returning the position in the array
        CurrentBorder = []
        x = 1
        # inital borders will always be the same
        # and the next edges are the
        if self.state == self.initial:
            BorderRight = self.initial[1][0]
            CurrentBorder.append(BorderRight)
            BorderDown = self.initial[0][1]
            CurrentBorder.append(BorderDown)
            self.Borders = CurrentBorder
            return self.Borders
        else:
            # need to call the edges
            return "cool"

    def initalNeighbors(self,row, col, state,action):
        # state = game board
        # action = new color
        board = [[c for c in row]
                 for row in state]
        oldColor = state[0][0]
        neighbors = []
        flood = []
        borders = []
        tally = 0
        neighbors += ([row + 1, col],)
        neighbors += ([row, col + 1],)
        neighbors += ([row - 1, col],)
        neighbors += ([row, col - 1],)
        #print(neighbors[1])
        for n in neighbors:
            #for r in range(len(neighbors)):
             #   for c in range(len(neighbors[0])):
            #print(len(neighbors))
            #print(n)
            #print(n[0])
            #print(n[1])
            # check if color of neighbor is color of original state
            if n == oldColor and n not in flood and n not in borders:
                flood.append([row, col], )
                self.getNeighbors(n[0], n[1], state, action, flood, borders) #will this feed flood and borders?
                #board[row, col] = action
            elif n != oldColor:
                tally += 1
            if tally == len(neighbors):
                borders.append([row, col], )
                #'tuple' object does not support item assignment
                #board[row, col] = action
                return (flood, borders)
        return flood, borders

    def getNeighbors(self,row, col, state,action, flood, borders):
        # state = game board
        # action = new color
        oldColor = state[0][0]
        neighbors = []
        flood = []
        borders = []
        tally = 0
        neighbors += ([row + 1, col],)
        neighbors += ([row, col + 1],)
        neighbors += ([row - 1, col],)
        neighbors += ([row, col - 1],)
        #print(neighbors[1])
        for n in neighbors:
            #for r in range(len(neighbors)):
             #   for c in range(len(neighbors[0])):
            #print(len(neighbors))
            #print(n)
            #print(n[0])
            #print(n[1])
            # check if color of neighbor is color of original state
            if n == oldColor and n not in flood and n not in borders:
                flood.append([row, col], )
                self.getNeighbors(n[0], n[1], state, action, flood, borders) #will this feed flood and borders?
                #state[row, col] = action
            elif n != oldColor:
                tally += 1
            if tally == len(neighbors):
                borders.append([row, col], )
                #state[row, col] = action
                return (flood, borders)
        return (flood, borders)

    def getColor(self, row, col):
        return "G"

    def changeColor(self, row, col):
        # change text to "G"
        return

    # check to see that all the state is the same color
    # def goal_test(self, state):
    #     if any(self.state != s for s in actions):
    #     for r in range(self.rows):
    #         if state[r] != self.goal[r]:
    #             return False
    #     return True


# board = []
# board += [Tile(('ca','_b'),('ab','c_'))]
# board[-1].label = '2x2 Tiles, 2 moves'


class Tile(search.Problem):
    blank = '_'
    moves = {
        'right': (0, -1),
        'left': (0, 1),
        'down': (-1, 0),
        'up': (1, 0),
    }

    def __init__(self, initial=None, goal=None, moves=10000):
        '''
        Initialize the tile puzzle.
        :param initial: a 2D sequence of characters
        representing tiles on a rectangular board.
        For example, ('123','45_') represents the board:
            1 2 3
            4 5 _
        Each board must contain exactly one _,
        and all other characters must be unique.
        :param goal: another 2D sequence of characters
        containing exactly the same tiles on a board of
        the same dimensions
        '''
        if goal == None:
            raise Exception('A goal must be specified.')
        rg, cg = self.tileCheck(goal)
        self.goal = goal
        self.rows = rg
        self.cols = cg

        if initial == None:
            initial = self.scramble(moves)
            print('initial state: %s' % str(initial))
        else:

            ri, ci = self.tileCheck(initial)
            assert ri == rg
            assert ci == cg

        self.initial = initial
        # print(self.initial)

    def actions(self, state):
        row, col = self.findBlank(state)
        actions = []
        if row > 0:
            actions.append('down')
        if col > 0:
            actions.append('right')
        if row < (self.rows - 1):
            actions.append('up')
        if col < (self.cols - 1):
            actions.append('left')
        return actions
        # return self.allowed(row, col)

    def result(self, state, action):
        board = [[t for t in row]
                 for row in state]
        rb, cb = self.findBlank(state)
        rd, cd = self.moves[action]
        rt, ct = rb + rd, cb + cd
        tile = board[rt][ct]
        board[rb][cb] = tile
        board[rt][ct] = self.blank
        newState = tuple([''.join(row)
                          for row in board])
        return newState

    def goal_test(self, state):
        for r in range(self.rows):
            if state[r] != self.goal[r]:
                return False
        return True

    def h(self, node):
        state = node.state
        count = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if state[r][c] == self.blank:
                    continue
                if state[r][c] != self.goal[r][c]:
                    count += 1

        return count

    def findBlank(self, state):
        for r in range(self.rows):
            for c in range(self.cols):
                if state[r][c] == self.blank:
                    return r, c
        raise Exception('%s not found in state: %s' %
                        (self.blank, state))

    def tileCheck(self, state):
        try:
            set().add(state)
        except:
            raise Exception(
                'This state is not hashable:\n    %s' % state)
        rows = len(state)
        cols = len(state[0])
        for row in state[1:]:
            assert cols == len(row)
        return rows, cols

    def scramble(self, howMany=10000):
        state = self.goal
        for i in range(howMany):
            actions = self.actions(state)
            children = [self.result(state, a)
                        for a in actions]
            state = random.choice(children)
        return state


# tiles = []
# tiles += [Tile(('ca','_b'),('ab','c_'))]
# tiles[-1].label = '2x2 Tiles, 2 moves'

# tiles += [Tile(('dce', '_ba'),('abc','de_'))]
# tiles[-1].label = '2x3 Tiles, 10 moves'

# tiles += [Tile(('abc', 'e_g', 'dhf'), ('abc','def','gh_'))]
# tiles[-1].label = '3x3 Tiles, 8 moves'

# tiles += [Tile(('dac','e_f','ghb'), ('abc','def','gh_'))]
# tiles[-1].label = '3x3 Tiles, 14 moves'

# tiles += [Tile(('_ab', 'dgf', 'ceh'), ('abc','def','gh_'))]
# tiles[-1].label = '3x3 Tiles, 16 moves'

# tiles += [Tile(('fch','b_g','ead'), ('abc','def','gh_'))]
# tiles[-1].label = '3x3 Tiles, 20 moves'

# tiles += [Tile(('hgb','dce','af_'), ('abc','def','gh_'))]
# tiles[-1].label = '3x3 Tiles, 22 moves'

# tiles += [Tile(('ecb', 'h_g', 'dfa'), ('abc','def','gh_'))]
# tiles[-1].label = '3x3 Tiles, 24 moves'

# tiles += [Tile(('abc', 'd_f', 'geh'), ('abc','def','gh_'))]
# tiles[-1].label = '3x3 Tiles, 2 moves'

# moves = 70
# tiles += [Tile(None, ('abc','def','gh_'), moves)]
# tiles[-1].label = '3x3 Tiles, %d moves' % moves

def flounder(problem, giveup=10000):
    'The worst way to solve a iProblem'
    node = search.Node(problem.initial)
    count = 0
    while not problem.goal_test(node.state):
        count += 1
        if count >= giveup:
            return None
        children = node.expand(problem)
        node = random.choice(children)
    return node


# fix this in your first commit and pull
# tiles += [Tile(('G','R'),('B','B'))]
flood = []
flood += [FloodGame(('G', 'G', 'R'))]  # 2nd batch was B G
flood[-1].label = '3x1 Tiles, 1 move1'

flood += [FloodGame(('GR', 'BR'))]
flood[-1].label = '2x2 Tiles, 2 moves'

flood += [FloodGame(('GRRO', 'BORO', 'BYYY', 'PPOP'))]
flood[-1].label = '4x4 Tiles, 5 moves'
names = [
    'David, Morris',
    'David, Muniz Macias',
]

searches = {}
searchMethods = {}

searches[names[0]] = [

    flood[0],
]

#searches[names[0]] = [
#    switch,
#    flood[0],
#    flood[1],
#    flood[2],
#]

searchMethods[names[0]] = [
    search.depth_first_graph_search,
    #search.breadth_first_search,
    #search.iterative_deepening_search,
    #search.uniform_cost_search,
    #search.astar_search,
    #flounder,
]

searches[names[1]] = [
    #flood[0],
    #flood[0],
]

searchMethods[names[1]] = [
    #search.astar_search,
]