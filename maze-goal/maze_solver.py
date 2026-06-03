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

    def manhattan_distance(self):
        return abs(self.environment.goal_position_y - self.agent_position_y) + abs(
            self.environment.goal_position_x - self.agent_position_x
        )