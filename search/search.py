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
        self.cost = cost

def getActionsForNode(node):
        #get the parent node of the winning node
        parentNode = node.parentNode
        #add the winning node's action to our list of actions
        listOfActions = [node.action]
        #as long as the parent node has an action (aka as long as it is not the Root Node) then:
        while parentNode.action != None:
            #get the action
            action = parentNode.action
            #add it to the list
            listOfActions.append(action)
            #get the next parent node
            parentNode = parentNode.parentNode
        #reverse the list of actions because the first action in the list is the winning node's action
        #and the last action in the list is the first action
        listOfActions.reverse()
        #return the list of actions
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
    from util import Stack
    from sets import Set
    #set up while loop variables
    success = False
    failure = False
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
    #initialize the explored dictionary
    explored = Set([])
    #make sure that we did not start at the goal
    if problem.isGoalState(startState):
        return listOfDirections
    #as long as we have not had success or failure then
    while success == False and failure == False:
        #if there is nothing in the frontier then stop the loop and return None
        if frontier.isEmpty():
            print "Error: Empty Frontier"
            failure = True
            return None
        #get the deepest node in the frontier
        node = frontier.pop()
        if problem.isGoalState(node.state):
            success = True
            listOfDirections = getActionsForNode(node)
            return listOfDirections
        #get the successors of this popped node's state
        if node.state not in explored:
            #add state to explored list
            explored.add(node.state)
            #expand state
            successors = problem.getSuccessors(node.state)
            #loop through the successors of this node
            for successor in successors:
                #declare state, action, and cost of this successor
                state, action, cost = successor
                #create a childNode of the popped node above
                childNode = Node(state, node, action, cost)
                #turn the state into a string to test if it is an exisiting key
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

"""

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue
    from sets import Set
    success = False
    failure = False
    startState = problem.getStartState()
    startNode = Node(startState,None,None,0)
    listOfDirections = []
    if problem.isGoalState(startState):
        return listOfDirections
    frontier = Queue()
    frontier.push(startNode)
    explored = Set([])
    while (success == False) and (failure == False):
        if frontier.isEmpty():
            print "Error: Frontier is empty"
            return None
        node = frontier.pop()
        if problem.isGoalState(node.state):
            listOfDirections = getActionsForNode(node)
            return listOfDirections
        if node.state not in explored:
            explored.add(node.state)
            successors = problem.getSuccessors(node.state)
            for successor in successors:
                state, action, cost = successor
                childNode = Node(state, node, action, cost)
                frontier.push(childNode)


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    from sets import Set
    success = False
    failure = False
    startState = problem.getStartState()
    startNode = Node(startState, None, None, 0)
    frontier = PriorityQueue()
    frontier.push(startNode, 0)
    explored = Set([])
    listOfDirections = []
    while (success == False) and (failure == False):
        if frontier.isEmpty():
            print "Error: Frontier is empty"
            failure = True
            return None
        node = frontier.pop()
        if problem.isGoalState(node.state):
            success = True
            listOfDirections = getActionsForNode(node)
            return listOfDirections
        if node.state not in explored:
            explored.add(node.state)
            successors = problem.getSuccessors(node.state)
            for successor in successors:
                state, action, cost = successor
                childPathCost = cost + node.cost
                childNode = Node(state, node, action, childPathCost)
                frontier.push(childNode, childPathCost)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    from util import PriorityQueue
    from sets import Set

    success = False
    failure = False
    startState = problem.getStartState()

    frontier = PriorityQueue()
    explored = Set()
    initialPathCost = 0 + heuristic(startState, problem)
    initialNode = Node(startState, None, None, initialPathCost)
    frontier.push(initialNode,initialPathCost)
    listOfDirections = []
    while success == False and failure == False:
        if frontier.isEmpty():
            print "Error: Empty Frontier"
            failure = True
            return None
        node = frontier.pop()
        if problem.isGoalState(node.state):
            listOfDirections = getActionsForNode(node)
            success = True
            return listOfDirections
        if node.state not in explored:
            explored.add(node.state)
            successors = problem.getSuccessors(node.state)
            for successor in successors:
                state, action, cost = successor
                childHeuristicCost = heuristic(state, problem)
                parentHeuristicCost = heuristic(node.state, problem)
                childPathCost = cost + node.cost + childHeuristicCost - parentHeuristicCost
                child = Node(state, node, action, childPathCost)
                if state not in explored:
                    frontier.push(child, childPathCost)



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
