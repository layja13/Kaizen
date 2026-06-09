from maze_solver import MazeSolverBase

class GreedySearch(MazeSolverBase):
    """
    It uses h(n) which is the heuristic function: 
    the estimated cost of the cheapest path from the state at node n to a goal state
    """
    def __init__(self, environment, show_movements=False):
        super().__init__(environment)
        self.starting_position = (self.agent_position_y, self.agent_position_x)
        self.show_movements = show_movements


    def solution(self):
        import heapq

        cost = self.manhattan_distance_abstract(self.agent_position_y, self.agent_position_x)
        frontier = []
        visited = {(self.agent_position_y, self.agent_position_x)}
        counter = 0

        heapq.heappush(frontier, (cost, counter, self.agent_position_y, self.agent_position_x))
        
        while frontier:
            _, _, y, x = heapq.heappop(frontier)

            if self.game_on_abstract(y, x):
                if self.environment.environment[y][x] == "G":
                    return True, self.starting_position, (y, x)
                
                if self.show_movements:
                    self.environment.environment[y][x] = "X"
                    for capa in self.environment.environment:
                        print(capa)
                    print("\n\n")

                for dy, dx in self.actions:
                    new_y = y + dy
                    new_x = x + dx
                    
                    if (new_y, new_x) not in visited:
                        counter += 1
                        visited.add((new_y, new_x))
                        cost = self.manhattan_distance_abstract(new_y, new_x)
                        heapq.heappush(frontier, (cost, counter, new_y, new_x))

        return False, False, False



class ASearch:
    """
    It uses h(n) which is the heuristic function and g(n), which is the accumulated cost function
    f(n) = h(h) + g(n), which is the estimated cost of the best path that continues from n to a goal 
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