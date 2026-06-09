from maze_solver import MazeSolverBase

class GreedySearch(MazeSolverBase):
    """
    It uses h(n) which is the heuristic function: 
    the estimated cost of the cheapest path from the state at node n to a goal state
    """
    def __init__(self, environment, show_movements=False):
        self.starting_position = (self.agent_position_y, self.agent_position_x)
        self.show_movements = show_movements
        super().__init__(environment)
        
        

class ASearch:
    """
    It uses h(n) which is the heuristic function and g(n), which is the accumulated cost function 
    """
    def __init__(self):
        pass


class BidirectionalASearch():
    def __init__(self):
        pass


class IDA(): # Iterative deepening A*
    def __init__(self):
        pass


class RBFS(): # Recursive best-first search 
    def __init__(self):
        pass