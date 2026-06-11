from maze_solver import MazeSolverBase

class BFS(MazeSolverBase):
    def __init__(self, environment, show_movements=False):
        super().__init__(environment)
        self.starting_position = (self.agent_position_y, self.agent_position_x)
        self.show_movements = show_movements

    def solution(self):
        from collections import deque

        queue = deque([(self.agent_position_y, self.agent_position_x)])
        visited = {(self.agent_position_y, self.agent_position_x)}
        expanded_nodes = -1

        while queue:
            current_position = queue.popleft()
            y = current_position[0]
            x = current_position[1]

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
                        queue.append((new_y, new_x))
                        visited.add((new_y, new_x))

        return False, False, False
                    


                
class DFS(MazeSolverBase):
    def __init__(self, environment, show_movements=False):
        super().__init__(environment)
        self.starting_position = (self.agent_position_y, self.agent_position_x)
        self.show_movements = show_movements

    def solution(self):
        stack = [self.starting_position]
        visited = {(self.agent_position_y, self.agent_position_x)}
        expanded_nodes = -1

        while stack:
            current_position = stack.pop()
            y, x = current_position
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
                        stack.append((new_y, new_x))
                        visited.add((new_y, new_x))
                    
        return False, False, False

                    

#
class DIJKSTRA(MazeSolverBase):  # Uniform-cost-search
    def __init__(self, environment, show_movements=False):
        super().__init__(environment)
        self.environment = environment
        self.show_movements = show_movements
        self.starting_position = (self.agent_position_y, self.agent_position_x)
                

    def solution(self):
        import heapq
        frontier = []
        visited = {self.starting_position:0}
        count = 0
        expanded_nodes = -1

        heapq.heappush(frontier, (0, count, (self.agent_position_y, self.agent_position_x)))
        count += 1

        while frontier:
            cost, _, position = heapq.heappop(frontier)
            y = position[0]
            x = position[1]
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

                    if (new_y, new_x) not in visited or cost + 1 < visited[(new_y, new_x)]:
                        heapq.heappush(frontier, (cost + 1, count, (new_y, new_x)))
                        count += 1
                        visited[(new_y, new_x)] = cost + 1
                    
        return False, False, False



class IDS(MazeSolverBase): # Iterative deepening search
    """
    This implementation can probably find a sub-optimal solution
    because the visited set can block a cell if it is reached first by a longer pathway
    """
    def __init__(self, environment, show_movements=False):
        super().__init__(environment)
        self.environment = environment
        self.starting_point = (self.agent_position_y, self.agent_position_x)
        self.show_movements = show_movements

    def solution(self, max_depth):

        def DLS(l):
            stack = [(self.starting_point, 0)]
            visited = {self.starting_point}


            while stack:
                node, depth = stack.pop()
                y, x = node
            

                if self.game_on_abstract(y, x):
                    if self.environment.environment[y][x] == "G":
                        return True, self.starting_point, (y, x)
                    
                    if depth >= l:
                        continue

                    if self.show_movements:
                        self.environment.environment[y][x] = "X"
                        for capa in self.environment.environment:
                            print(capa)
                        print("\n\n")
                    

                    for dy, dx in self.actions:
                        new_y = y + dy
                        new_x = x + dx
                        if (new_y, new_x) not in visited:
                            stack.append(((new_y, new_x), depth + 1))
                            visited.add((new_y, new_x))
        
        for l in range(max_depth + 1):
            ans = DLS(l)
            if ans:
                return ans
        return False





class BidirectionalSearch():
    def __init__(self):
        pass