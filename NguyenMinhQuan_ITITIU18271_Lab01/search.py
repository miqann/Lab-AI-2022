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

REVERSE_PUSH = True


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

# ______________________________________________________________________________


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    fringe = util.Stack()
    graph = GraphSearch(problem, fringe)
    return graph.search()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    fringe = util.Queue()
    graph = GraphSearch(problem, fringe)
    return graph.search()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    fringe = util.PriorityQueue()
    graph = GraphSearch(problem, fringe)
    return graph.search()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    fringe = util.PriorityQueue()
    graph = GraphSearch(problem, fringe, heuristic)
    return graph.search()

def greedyBFS(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    fringe = util.PriorityQueue()
    graph = GreedyBFS(problem, fringe, heuristic)
    return graph.search()

# Abbreviations
brfs = breadthFirstSearch
dfs = depthFirstSearch
ucs = uniformCostSearch
bfs = greedyBFS
astar = aStarSearch


############
class Node:
    parent = None
    state = None
    action = None
    step_cost = None
    path_cost = 0
    def __init__(self, parent, state, action, step_cost, path_cost):
        self.parent = parent
        self.state = state
        self.action = action
        self.step_cost = step_cost
        self.path_cost = path_cost


class GraphSearch:
    def __init__(self, problem, fringe, heuristic=None):
        self.problem = problem
        self.fringe = fringe
        self.explored = util.Counter()
        self.frontier = util.Counter()
        self.heuristic = heuristic

    def _addToFringe(self, node):
        #Add node to the fringe. Be careful with the type of fringe, you should check it for a suitable addition.
        if isinstance(self.fringe, util.Stack) or isinstance(self.fringe, util.Queue): #DFS/BFS
            self.fringe.push(node)
        else:
            if self.heuristic is None: #UCS
                self.fringe.push(node, node.path_cost)
            else: #UCS
                g = node.path_cost
                h = self.heuristic(node.state, self.problem)
                f = g + h
                self.fringe.push(node, f)
                
    def search(self):
        #Implement main graph search algorithm
        initial = self.problem.getStartState()
        node = Node(None, initial, None, 0, 0)
        self._addToFringe(node)
        self.frontier[hash(initial)] = node
        while not self.fringe.isEmpty():
            current = self.fringe.pop()
            self.explored[hash(current.state)] = current
            self.frontier.pop(hash(current.state), None)
            
            if self.problem.isGoalState(current.state): return self.___extractPath(current)
            self.___expand(current) #expand current
        return []
            
    def ___extractPath(self, node):
        #extract the path to a specific node
        #this function should return the path (list) to the node
        stack = util.Stack()
        while node is not None:
            stack.push(node.action)
            node = node.parent
        path = []
        while not stack.isEmpty():
            action = stack.pop()
            if action is not None: path.append(action)
        return path
    
    def ___expand(self, node):
        #expand the branch from a node
        successors = self.problem.getSuccessors(node.state)
        for triple in successors:
            child_state, action, step_cost = triple
            key = hash(child_state)
            if self.explored[key] == 0:
                #not visited before
                child_node = Node(node, child_state, action, step_cost, node.path_cost + step_cost)
                if self.frontier[key] == 0:
                    #not generated before
                    self._addToFringe(child_node)
                    self.frontier[key] = child_node
                else:
                    #generated before
                    if isinstance(self.fringe, util.Stack): #DFS
                        self._addToFringe(child_node)
                    elif isinstance(self.fringe, util.Queue): #BFS
                        pass
                    else:
                        #update for UCS
                        old_node = self.frontier[key]
                        if child_node.path_cost < old_node.path_cost:
                            self.fringe.update(child_node, child_node.path_cost)
                            self.frontier.pop(hash(old_node.state), None) #remove from frontier
                            self.frontier[hash(child_node.state)] = child_node

class GreedyBFS(GraphSearch):
    def __init__(self, problem, fringe, heuristic=None):
        super(GreedyBFS, self).__init__(problem, fringe, heuristic)

    def _addToFringe(self, node):
        #Add node to the fringe. Be careful with the type of fringe, you should check it for a suitable addition.
        if isinstance(self.fringe, util.Stack) or isinstance(self.fringe, util.Queue): #DFS/BFS
           self.fringe.push(node)
        else:
            if self.heuristic is None: #UCS
                self.fringe.push(node, node.path_cost)
            else: #BFS
                g = 0
                h = self.heuristic(node.state, self.problem)
                f = g + h
                self.fringe.push(node, f)
