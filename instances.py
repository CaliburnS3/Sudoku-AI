import search
import sys
import traceback
import math


class Sudoku(search.Problem):
    # TODO: Implement sub-box algorithm
    #  square root of row/col, basic grid etc.
    # TODO: more puzzles
    # TODO: a way to make searching faster,
    #  such as having two options in 1 square,
    #  but if using one answer, it makes another impossible
    # initial state constructor inherited
    def __init__(self, initial):
        self.rows = len(initial)
        self.cols = len(initial[0])
        self.initial = initial
        # self.actions(initial)

    def actions(self, state):
        # New version:
        # Checks both row and column, eliminating possiblities from both

        # Finding blank, so that we have values to work off of
        row, col = self.findBlank(state)

        # Constructing board
        board = [[t for t in row]
                 for row in state]

        # Fills the "answer list" with all possible values of a sudoku
        answerList = []
        for i in range(self.rows):
            answerList.append(i + 1)

        # Row check
        for i in range(self.cols):
            rowTest = int(board[i][col])
            if rowTest in answerList:
                answerList.remove(rowTest)

        # Col check
        for i in range(self.rows):
            colTest = int(board[row][i])
            if colTest in answerList:
                answerList.remove(colTest)

        # Box check
        # Finding sub-box sizes.
        rowSquare = int(math.sqrt(self.rows))
        colSquare = int(math.sqrt(self.cols))
        
        # Getting the box position of the blank's box
        rowBox, colBox = self.findBlank(state)
        rowBox, colBox = rowBox % rowSquare, colBox % colSquare

        # Searching puzzle for all slots in box
        for r in range(self.rows):
            for c in range(self.cols):
                if r % rowSquare == rowBox and c & colSquare == colBox:
                    if state[r][c] in answerList:
                        answerList.remove(state[r][c])
                        
        # This returns the created output as a list
        return answerList

    def result(self, state, action):
        board = [[t for t in row]
                 for row in state]
        oldState = tuple([''.join(row)
                          for row in board])
        # Finds the first blank, assigning it a new value and updating the game state
        rb, cb = self.findBlank(state)
        board[rb][cb] = str(action)
        newState = tuple([''.join(row)
                          for row in board])

        # print('oldState = ' + str(oldState))
        # print('newState = ' + str(newState))
        # print('')
        return newState

    def findBlank(self, state):
        for r in range(self.rows):
            for c in range(self.cols):
                if state[r][c] == '0':
                    return r, c
        return False

    def goal_test(self, state):
        if not self.findBlank(state):
            # if there are no '0' left, we have solved it
            return True
        return False


# initialState = ('1030', '0210', '4100', '0000'
# initialState = ('0000', '0000', '0000', '0000')
# initialState = ('1432', '3214', '4123', '2300')
# instance = Sudoku(initialState)
# instance.label = '4x4 Sudoku, 2 step gap'


puzzle0 = (
    '0200',
    '3000',
    '0000',
    '0000')

# 3x3 unsolved.png
puzzle1 = (
    '213', 
    '100', 
    '321')
# 4x4 unsolved.jpeg
puzzle2 = (
    '1430', 
    '0210', 
    '4100', 
    '0000')
puzzle3 = (
    '123564',
    '650213',
    '530421',
    '400356',
    '365142',
    '241635'
    # 6x6 unsolved
)
puzzle4 = (
    '254680190',
    '607915042',
    '913027568',
    '345071906',
    '720349050',
    '890206073',
    '508764219',
    '162508034',
    '479132685',
    # 9x9 unsolved
)
puzzle5 = (
    '250600190',
    '000900042',
    '913027568',
    '345001906',
    '726349050',
    '890206073',
    '508764219',
    '162508034',
    '479132685'
)
# 9x9 unsolved.png
puzzle6 = (
    '530070000',
    '600195000',
    '098000060',
    '800060003',
    '400803001',
    '700020006',
    '060000280',
    '000419005',
    '000080079')

# Multiple instances
instance0 = Sudoku(puzzle0)
# instance0.label("4x4 Can only be solved through box method.")

instance1 = Sudoku(puzzle1)
# instance1.label("3x3, 2 gaps")
instance2 = Sudoku(puzzle2)
# instance2.label("4x4, 5 gaps")
instance3 = Sudoku(puzzle3)
# instance3.label("6x6, 4 gaps")
instance4 = Sudoku(puzzle4)
# instance4.label("9x9 16 gaps (Might break everything.")
instance5 = Sudoku(puzzle5)
# instance5.label("9x9 22 gap (Will probably break everything.")

# instance = Sudoku(puzzle3)
# instance.label = '9x9 Sudoku, many many steps.'

names = [
    # Change to your name
    'Ingram, Clark',
    'Murdock, Adam',
    # Add names to group different instances
    # with different search methods.
]

searches = {}
searchMethods = {}

searches[names[0]] = [
    instance0,
    instance1,
    instance2,
    instance3,
    instance4,
    instance5,
]

searchMethods[names[0]] = [
    search.depth_first_graph_search,
    search.breadth_first_search,
    search.iterative_deepening_search,
    search.uniform_cost_search,
    # search.astar_search,
]

####################################################
#
# Modules in the examples folder
# Import them for testing only.

# from examples import lightSwitch
# names += lightSwitch.names
# searches.update(lightSwitch.searches)
# searchMethods.update(lightSwitch.searchMethods)

# from examples import fifteen
# names += fifteen.names
# searches.update(fifteen.searches)
# searchMethods.update(fifteen.searchMethods)

# from examples import nqueens
# names += nqueens.names
# searches.update(nqueens.searches)
# searchMethods.update(nqueens.searchMethods)

# from examples import flounder
# for key in searchMethods:
#     searchMethods[key] += [flounder.flounder]
