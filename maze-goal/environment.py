import random

class Environment:
    def __init__(self, height, width, difficulty, seed, agent_position_y=None, agent_position_x=None, goal_position_y=None, goal_position_x=None):
        self.rng = random.Random(seed)
        self.height = height
        self.width = width
        self.agent_position_y = agent_position_y
        self.agent_position_x = agent_position_x
        self.goal_position_y = goal_position_y
        self.goal_position_x = goal_position_x
        self.difficulty = difficulty 
        self.environment = self.create_environment()
        self._place_agent()
        self._place_goal()


    def create_environment(self):
        return [["_" if random.randint(0, 10) > self.difficulty else "O" for i in range(self.width)] for i in range(self.height)]
    
    def show_environment(self):
        for layer in self.environment:
            print(layer)
    

    def _place_agent(self):
        # It checks to not overwrite any obstacle or goal
        if not self.agent_position_x or not self.agent_position_y:
            self.agent_position_y = self.rng.randint(0, self.height - 1)
            self.agent_position_x = self.rng.randint(0, self.width - 1)

            while self.environment[self.agent_position_y][self.agent_position_x] == "O" or \
                self.environment[self.agent_position_y][self.agent_position_x] == "M":

                self.agent_position_y = self.rng.randint(0, self.height - 1)
                self.agent_position_x = self.rng.randint(0, self.width - 1)
        
        self.environment[self.agent_position_y][self.agent_position_x] = "A"
        return


    def _place_goal(self):
        # It checks to not overwrite any obstacle or agent
        if not self.goal_position_x or not self.goal_position_y:
            self.goal_position_y = self.rng.randint(0, self.height - 1)
            self.goal_position_x = self.rng.randint(0, self.width - 1)

            while self.environment[self.goal_position_y][self.goal_position_x] == "O" or \
                self.environment[self.goal_position_y][self.goal_position_x] == "A":

                self.goal_position_y = self.rng.randint(0, self.height - 1)
                self.goal_position_x = self.rng.randint(0, self.width - 1)
        
        self.environment[self.goal_position_y][self.goal_position_x] = "M"
        return
    