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

        heuristics = self.manhattan_distance_abstract(self.agent_position_y, self.agent_position_x)
        frontier = []
        visited = {(self.agent_position_y, self.agent_position_x)}
        counter = 0
        expanded_nodes = -1

        heapq.heappush(frontier, (heuristics, counter, self.agent_position_y, self.agent_position_x))
        
        while frontier:
            _, _, y, x = heapq.heappop(frontier)
            expanded_nodes += 1

            if self.game_on_abstract(y, x):
                if self.environment.environment[y][x] == "G":
                    return True, self.starting_position, (y, x), expanded_nodes
                
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
                        heuristics = self.manhattan_distance_abstract(new_y, new_x)
                        heapq.heappush(frontier, (heuristics, counter, new_y, new_x))

        return False, False, False



class AStar(MazeSolverBase):
    """
    It uses h(n) which is the heuristic function and g(n), which is the accumulated cost function
    f(n) = h(h) + g(n), which is the estimated cost of the best path that continues from n to a goal 
    """
    def __init__(self, environment, show_movements=False):
        super().__init__(environment)
        self.starting_position = (self.agent_position_y, self.agent_position_x)
        self.show_movements = show_movements

    def solution(self):
        expanded_nodes = -1
        import heapq

        heuristics = self.manhattan_distance_abstract(self.agent_position_y, self.agent_position_x)
        cost = 0

        frontier = []
        visited = {(self.agent_position_y, self.agent_position_x):0}
        counter = 0

        heapq.heappush(frontier, (heuristics + cost, counter, cost, self.agent_position_y, self.agent_position_x))

        while frontier:
            f, _, g, y, x = heapq.heappop(frontier)
            expanded_nodes += 1

            if self.game_on_abstract(y, x):
                if self.environment.environment[y][x] == "G":
                    return True, self.starting_position, (y, x), expanded_nodes
                
                if self.show_movements:
                    self.environment.environment[y][x] = "X"
                    for capa in self.environment.environment:
                        print(capa)
                    print("\n\n")
                    
                for dy, dx in self.actions:
                    new_y = dy + y
                    new_x = dx + x

                    new_g = g + 1

                    if (new_y, new_x) not in visited or new_g < visited[(new_y, new_x)]:
                        counter += 1
                        visited[(new_y, new_x)] = new_g
                        new_h = self.manhattan_distance_abstract(new_y, new_x)
                        heapq.heappush(frontier, (new_h + new_g, counter, new_g, new_y, new_x))
        return False



class BidirectionalASearch():
    def __init__(self):
        pass


class IDA(MazeSolverBase): # Iterative deepening A*
    def __init__(self, environment, show_movements=False):
        super().__init__(environment)
        self.starting_point = (self.agent_position_y, self.agent_position_x)
        self.show_movements = show_movements

    
    def search(self, start, threshold, g):
        y, x = start
        
        if self.game_on_abstract(y, x):
            self.expanded_nodes += 1 
            h = self.manhattan_distance_abstract(y, x)
            f = h + g
            min_threshold_exceeded = float("inf")
            self.expanded_nodes += 1

            if f > threshold:
                return None, f, None

            if self.environment.environment[y][x] == "G":
                return True, threshold, (y, x)
        
            if self.show_movements:
                self.environment.environment[y][x] = "X"
                for capa in self.environment.environment:
                    print(capa)
                print("\n\n")
            
            for dy, dx in self.actions:
                new_y = y + dy
                new_x = x + dx
                new_g = g + 1

                if (new_y, new_x) not in self.best_route_costs or new_g < self.best_route_costs[(new_y, new_x)]:
                    self.best_route_costs[(new_y, new_x)] = new_g

                    found, new_threshold, goal = self.search((new_y, new_x), threshold, new_g)

                    if found:
                        return found, threshold, goal
                    
                    min_threshold_exceeded = min(min_threshold_exceeded, new_threshold)

            return None, min_threshold_exceeded, None
        
        return None, float("inf"), None



    def solution(self):
        threshold = self.manhattan_distance_abstract(self.agent_position_y, self.agent_position_x)
        self.expanded_nodes = -1

        while True:
            self.best_route_costs = {self.starting_point:0}

            found, new_threshold, goal = self.search(self.starting_point, threshold, g=0)

            if found:
                return found, threshold, goal
            
            threshold = new_threshold

            if threshold == float("inf"):
                return False, False, False


class RBFS(MazeSolverBase): # Recursive best-first search 
    def __init__(self, environment, show_movements=False):
        super().__init__(environment)
        self.environment = environment
        self.show_movements = show_movements

    def solution(self):
        g = 0
        h = self.manhattan_distance_abstract(self.agent_position_y, self.agent_position_x)

        result, f = self.search(self.agent_position_y, self.agent_position_x, h + g, g, float("inf"))

        return result, f
    
    def search(self, y, x, f, g, f_limit):
        successors = []

        if self.environment.environment[y][x] == "G":
            return True, (y, x)

        if self.show_movements:
            self.environment.environment[y][x] = "X"
            for capa in self.environment.environment:
                print(capa)
            print("\n\n")
        
        for dy, dx in self.actions:
            new_y = dy + y 
            new_x = dx + x
            if self.game_on_abstract(new_y, new_x):
                child_g = g + 1
                child_f = self.manhattan_distance_abstract(new_y, new_x) + child_g
                child_f = max(child_f, f)

                successors.append([new_y, new_x, child_f, child_g])
        
        while True:
            successors.sort(key=lambda child:child[2])

            best_y, best_x, best_f, best_g = successors[0]

            if best_f > f_limit:
                return None, best_f

            if len(successors)>1:
                alternative_f = successors[1][2]
            else:
                alternative_f = float("inf")

            result, best_f = self.search(best_y, best_x, best_f, best_g, min(f_limit, alternative_f))
            
            successors[0][2] = best_f

            if result != None:
                return result, best_f
            
        





