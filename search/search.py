# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

class Node:
    """
    Attributes: state - the state of that node
                parentNode - the node from which we got here
    """
    def __init__(self, state, parentNode, action, cost):
        self.state = state
        self.parentNode = parentNode
        self.action = action

def getActionsForNode(node):
        parentNode = node.parentNode
        listOfActions = []
        while parentNode.parentNode != None:
            action = parentNode.action
            listOfActions.append(action)
            parentNode = parentNode.parentNode
        listOfActions.reverse()
        print listOfActions
        return listOfActions

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    #get the needed class
    from game import Directions
    from game import Actions
    from pacman import GameState
    from util import Stack
    #set up while loop variables
    success = False
    failure = False
    #set up the four Directions
    north = Directions.NORTH
    east = Directions.EAST
    south = Directions.SOUTH
    west = Directions.WEST
    #get the start state
    startState = problem.getStartState()
    #initialize the list that we will want to return
    listOfDirections = []
    #create the initial node
    startNode = Node(startState, None, None, 0)
    #initialize the frontier
    frontier = Stack()
    #put initial state in the frontier
    frontier.push(startNode)
    #initialize the explored set
    explored = []
    #make sure that we did not start at the goal
    if problem.isGoalState(startState):
        return listOfDirections
    while success == False and failure == False:
        if frontier.isEmpty():
            print "Error: Empty Frontier"
            failure = True
            return None
        node = frontier.pop()
        explored.append(node.state)
        successors = problem.getSuccessors(node.state)
        for successor in successors:
            state, action, cost = successor
            if action == None:
                print "None"
                break
            childNode = Node(state, node, action, cost)
            contains = False
            for exploredState in explored:
                if exploredState == state:
                    contains = True
            if contains == False:
                if problem.isGoalState(state):
                    print "*"*60
                    print "goal state"
                    print "*"*60
                    success = True
                    listOfDirections = getActionsForNode(childNode)
                    return listOfDirections
                frontier.push(childNode)
"""
    def depthFirstSearch(problem):
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    "*** YOUR CODE HERE ***"


    print type(problem.getStartState())
    print problem.getStartState()

    sucs = problem.getSuccessors(problem.getStartState())

    actions = []
    for suc in sucs:
        state = suc[0]
        action = suc[1]
        stepCost = suc[2]

        state, action, stepCost = suc
        newsucs = problem.getSuccessors(state)
        actions.append(action)

    return actions
"""

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
