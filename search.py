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

def depthFirstSearch(problem: SearchProblem):
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
    "* YOUR CODE HERE *"
    
    visited = set()  # set noduri vizitate
    stack = util.Stack()  #stiva pt cautare in adancime
    stack.push((problem.getStartState(),[])) #adaugare nod start pe stiva

    while not stack.isEmpty():
        state, path = stack.pop() #socatere nod
        # stare curenta= stare tinta?
        if problem.isGoalState(state):
             return path       #nod tinta, returneaza cale
        #marcare nod ca vizitat
        if state not in visited:
            visited.add(state)
            #adaugare succesori
            for neighbor, action, _ in problem.getSuccessors(state):
                stack.push((neighbor, path+[action]))

    return None

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "* YOUR CODE HERE *"
    visited = set()
    queue = util.Queue()  #coada pt cautare in latime
    queue.push((problem.getStartState(), []))#adaugare nod start 

    while not queue.isEmpty():
        state, path= queue.pop() #scoatere nod 
        #stare curenta = goal state?
        if problem.isGoalState(state):
            return path 
        #marcare nod ca vizitat
        if state not in visited:
            visited.add(state)
            #adaugare succesori
            for neighbor, action, _ in problem.getSuccessors(state):
                queue.push((neighbor, path+[action]))

    return []


def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "* YOUR CODE HERE *"

    visited = set()
    priority_queue = util.PriorityQueue() #coada priotitate pt ucs
    #adaugare nod start prioritate 0 in coada
    priority_queue.push((problem.getStartState(), [],0),0)
    cost_so_far = {problem.getStartState(): 0} #dictionar verificare daca deja exista drum mai ieftin 

    while not priority_queue.isEmpty():
        state, path, cost = priority_queue.pop() #scoatem 
        #stare curenta = stare goal?
        if problem.isGoalState(state):
            return path 
        #marcare nod ca vizitat
        if state not in visited or cost_so_far(state, float('inf')):
            visited.add(state)
            cost_so_far[state] = cost
            #adaugare succesori
            for neighbor, action, step_cost in problem.getSuccessors(state):
                new_cost = cost + step_cost
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    priority_queue.push((neighbor, path + [action], new_cost),new_cost + heuristic(neighbor, problem))
                    cost_so_far[neighbor] = new_cost
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "* YOUR CODE HERE *"

    visited = set()
    priority_queue = util.PriorityQueue() #creare coada prioritate
    start_state = problem.getStartState()
    #adaugare nod start
    #valoare cost+euristica
    start_priority = heuristic(start_state, problem)
    priority_queue.push((start_state, [], 0), start_priority)  # Salvăm starea, drumul și costul
    

    while not priority_queue.isEmpty():
        state,path,cost = priority_queue.pop() #scoatere
        #st curenta = goal state?
        if problem.isGoalState(state):
            return path 

        if state not in visited:  #marcare nod vizitat
            visited.add(state)
            #adaug succesori
            for neighbor, action, step_cost in problem.getSuccessors(state):
                new_cost = cost + step_cost
                priority_queue.push((neighbor, path + [action], new_cost),
                new_cost + heuristic(neighbor, problem))  # cost combinat (cost + euristică)
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch