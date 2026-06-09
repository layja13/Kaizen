"""
When a function's name end with "abstract" means that the coordenates of the agent
in the environment are not used nor change, instead uses the coordenates given as parameters
"""

class MazeSolverBase:
    def __init__(self, environment):
        self.environment = environment
        self.agent_position_y = environment.agent_position_y
        self.agent_position_x = environment.agent_position_x

        self.actions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        self.actions_interpretable = {
            (-1, 0): "UP",
            (1, 0): "DOWN",
            (0, 1): "RIGHT",
            (0, -1): "LEFT",
        }

    def reset_agent_position(self):
        self.agent_position_y = self.environment.agent_position_y
        self.agent_position_x = self.environment.agent_position_x

    def move(self, action):
        dy, dx = action
        self.agent_position_y += dy
        self.agent_position_x += dx

    def game_on(self):
        if (
            self.agent_position_y < 0
            or self.agent_position_x < 0
            or self.agent_position_y >= self.environment.height
            or self.agent_position_x >= self.environment.width
            or self.environment.environment[self.agent_position_y][self.agent_position_x] == "O"
        ):
            return False

        return True


    def game_on_abstract(self, pos_y, pos_x):
        if (
            pos_y < 0
            or pos_x < 0
            or pos_y >= self.environment.height
            or pos_x >= self.environment.width
            or self.environment.environment[pos_y][pos_x] == "O"
        ):
            return False

        return True


    def win(self):
        if self.environment.environment[self.agent_position_y][self.agent_position_x] == "G":
            return True
        return False

    def manhattan_distance(self):
        return abs(self.environment.goal_position_y - self.agent_position_y) + abs(
            self.environment.goal_position_x - self.agent_position_x)


    def manhattan_distance_abstract(self, y, x):
        return abs(self.environment.goal_position_y - y) + abs(
            self.environment.goal_position_x - x)