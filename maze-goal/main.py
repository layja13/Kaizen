from environment import Environment

# Global variables

WIDTH = 10
HEIGHT = 10
SEED = 0
AGENT_POSITION_X = 2
AGENT_POSITION_Y = 2
GOAL_POSITION_X = 8
GOAL_POSITION_Y = 8

# Environment
environment = Environment(width=WIDTH, height=HEIGHT, seed=SEED, difficulty=5, agent_position_x=AGENT_POSITION_X, agent_position_y=AGENT_POSITION_Y, goal_position_x=GOAL_POSITION_X, goal_position_y=GOAL_POSITION_Y)
environment.show_environment()