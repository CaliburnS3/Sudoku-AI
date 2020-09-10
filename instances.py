import search
import sys
import traceback


class Sudoku(search.Problem):

    # initial state constructor inherited
    def __init__(self, initial):
        self.rows = len(initial)
        self.cols = len(initial[0])
        self.initial = initial
        print('initial = ' + str(initialState))
        self.actions(initial)


    def actions(self, state):
        # New version:
        # Checks both row and column, eliminating possiblities from both
        # If it finishes with only 1 output possible, fill.
        # Otherwise, put an X

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

        # Now, if answerList has only 1 value, fill, otherwise X
        if len(answerList) == 1:
            output = str(answerList[0])

        else:
            output = 'X'

        # This returns the created output
        # self.result(state, output)
        return output
        # return []

    def result(self, state, action):
        board = [[t for t in row]
                 for row in state]
        oldState = tuple([''.join(row)
                          for row in board])
        # Finds the first blank, assigning it a new value and updating the game state
        rb, cb = self.findBlank(state)
        board[rb][cb] = action
        newState = tuple([''.join(row)
                          for row in board])
        #TODO figure out how to assign state to outcome????
        print('oldState = ' + str(oldState))
        print('newState = ' + str(newState))
        print('')
        return newState

    def convert(self, state):
        # Converting all the 'X' back into '0' for another round of sudoku
        board = [[t for t in row]
                 for row in state]
        for r in range(self.rows):
            for c in range(self.cols):
                if state[r][c] == 'X':
                    rb, cb = r, c
        board[rb][cb] = '0'
        newState = tuple([''.join(row)
                          for row in board])
        return newState

    def findBlank(self, state):
        for r in range(self.rows):
            for c in range(self.cols):
                if state[r][c] == '0':
                    return r, c
        return False

    def goal_test(self, state):
        if not self.findBlank(state):
            #??????? updating state to convert X back to 0
            state = self.convert(state)

        if not self.findBlank(state):
            # if after conversion, there are no '0' left, we have solved it
            return True
        return False


initialState = ('1030', '0210', '4100', '0000')
instance = Sudoku(initialState)
instance.label = '4x4 Sudoku, 10 gap'

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
    instance,
]

searchMethods[names[0]] = [
    search.depth_first_graph_search,
    #search.breadth_first_search,
    #search.iterative_deepening_search,
    #search.uniform_cost_search,
    #search.astar_search,
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
