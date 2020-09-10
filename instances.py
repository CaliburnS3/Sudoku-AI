import search
import random
import sys, traceback

# TODO
# create a grid
# • Create problems that are:
#   - 2 moves from solution
#   - 4-8 moves from solution
#   - 16-32 moves from solution

# Problem:
# Basically Sudoku. The goal is to have a unique number 
# in the range of 1 to n, n being the size of the Sudoku.

#First
#scan. start in a corner and go to each blank, check to see if there is an easy to spot outcome, else move on

#Idea for structuring
#tiles += [Tile(('2*3', '1**', '**1'),('213', '132', '321'))]
#Sudoku = ['2*3', ['1**', ['**1']]], ['213', ['132', ['321']]]
#print(L[2])
# Prints ['cc', 'dd', ['eee', 'fff']]

# Each cell stored as tuple 
# A1 = (a,1,3)
# cell = (row, col, val);

# Using zero since it is an integer we will never use

# Sudoku = []

#print(L[2][2])
# Prints ['eee', 'fff']

#print(L[2][2][0])
# Prints eee
#https://www.learnbyexample.org/python-nested-list/
# tiles[-1].label = '3x3 sudoku, * moves to solve, not counting agent movement'

class Solo(search.Problem):
    
    moves = {

    }

    def actions(self, state):
        row, col = self.findBlank(state)
        actions = []
    

    def __init__(self, intial=None, goal=None, moves=10):

        if goal==none:
            raise Exception('A goal must be specified homeslice.')

        self.goal = goal;
        self.rows = rg
        self.cols = cg

        def actions(self,state):
            return

        def result(self, state, action):
            return

        def goal_test(self, state):
            for r in range(self.rows):
                if state[r] != self.goal[r]:
                    return False
            return True
        

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





# First. we findBlank, it returns the position of the first found "blank", in this case 0
#TODO Then, it checks the row and column, determining if there is only 1 missing value.
#TODO If so, it runs result, replacing that 0 with that value
#TODO If no, it runs result, replacing that 0 with an "x"
#TODO It continues the sweep, rinsing and repeating
#TODO Once it makes its first initial sweep, it sweeps again, replacing all "x" with 0
#TODO One final sweep, if there are no "0" then the puzzle is complete

#TODO Moves can be the number options, the option to write x, or to replace x with 0
#TODO actions can be the brain that checks the rows and columns.





class Tile(search.Problem):
    blank = '0'
    moves = {
        'action1': ('1'),
        'action2': ('2'),
        'action3': ('3'),
        'action4': ('4'),
        'action5': ('5'),
        'action6': ('6'),
        'action7': ('7'),
        'action8': ('8'),
        'action9': ('9'),
        'action0': ('0'),
        'actionX': ('X'),
        
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

        #TODO - remove, this scrambles the results, WE DO NOT WANT THAT
        if initial == None:
            # initial = self.scramble(moves)
            # print('initial state: %s' % str(initial))
            print('Line 137')
        else:
            ri, ci = self.tileCheck(initial)
            assert ri == rg
            assert ci == cg

        self.initial = initial

    def actions(self, state):
        row, col = self.findBlank(state)

        # problemArray[index] = new_value
        
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

    def actions(self, state):
        row, col = self.findBlank(state)
        actions = []
        board = [[t for t in row]
                 for row in state]
                 
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
        board[rb][cb] = self.moves[action]
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

    # def scramble(self, howMany=10000):
    #     state = self.goal
    #     for i in range(howMany):
    #         actions = self.actions(state)
    #         children = [self.result(state,a)
    #                     for a in actions]
    #         state = random.choice(children)
    #     return state




tiles = []

tiles += [Tile(('1432','0014','4123','2300'), ('1432','3214','4123','2341'))]
tiles[-1].label = '4x4 Sudoku'

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
names = [
    'Ingram, Franklin Clarkie',
    'Murdock, Atom',
]

searches = {}
searchMethods = {}

searches[names[0]] = [
    switch,
    tiles[0],
    # tiles[1],
]

searchMethods[names[0]] = [
    search.depth_first_graph_search,
    search.breadth_first_search,
    search.iterative_deepening_search,
    search.uniform_cost_search,
    search.astar_search,
    flounder,
]

searches[names[1]] = [
    # tiles[-6],
    # tiles[-3],
]

searchMethods[names[1]] = [
    search.astar_search,
]
