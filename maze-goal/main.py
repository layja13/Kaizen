from environment import Environment
from solutions.genetic_algorithms import SimpleGeneticAlgorithm, MicrobialGeneticAlgorithm
import matplotlib.pyplot as plt

# -------------------------------------------------
# Environment
# Global variables
WIDTH = 10
HEIGHT = 10
SEED = 1
AGENT_POSITION_X = 2
AGENT_POSITION_Y = 2
GOAL_POSITION_X = 8
GOAL_POSITION_Y = 8
DIFFICULTY = 3


# ---------------------------------------------------------------------
# Simple Genetic Algorithm
# Global variables
MUTATION_RATE = 0.05
POP_SIZE = 100
NUM_GENES = 20
NUM_GENERATIONS = 500

"""
# Simple Genetic Algorithm

# Environment
environment = Environment(width=WIDTH, height=HEIGHT, seed=SEED, difficulty=DIFFICULTY, agent_position_x=AGENT_POSITION_X, agent_position_y=AGENT_POSITION_Y, goal_position_x=GOAL_POSITION_X, goal_position_y=GOAL_POSITION_Y)
#environment.show_environment()

sga = SimpleGeneticAlgorithm(environment=environment, mutation_rate=MUTATION_RATE, pop_size=POP_SIZE, num_genes=NUM_GENES, num_generations=NUM_GENERATIONS)
#sga.show_poblation(interpretable=True)

solution = sga.evolve()

print(f"Simple Genetic Algorithm (Population Based Search) Solution")
print(f"Goal reached: {sga.win}")
print(f"solution: {solution}")

sga.show_interpretable_genome(solution)

plt.plot([generation for generation in range(NUM_GENERATIONS)], sga.fitness_evolution_per_generation)
plt.show()
"""

# ---------------------------------------------------------------------
# Microbial Genetic Algorithm
# Global variables
SHARING_GENES_RATE = 0.3
NUM_TOURNAMENTS = 2000

"""
# Environment
environment = Environment(width=WIDTH, height=HEIGHT, seed=SEED, difficulty=DIFFICULTY, agent_position_x=AGENT_POSITION_X, agent_position_y=AGENT_POSITION_Y, goal_position_x=GOAL_POSITION_X, goal_position_y=GOAL_POSITION_Y)
#environment.show_environment()

mga = MicrobialGeneticAlgorithm(environment=environment, mutation_rate=MUTATION_RATE, pop_size=POP_SIZE, num_genes=NUM_GENES, num_tournaments=NUM_TOURNAMENTS, sharing_genes_rate=SHARING_GENES_RATE)

solution = mga.evolve()
print(f"Microbial Genetic Algorithm Solution")
print(f"Goal reached: {mga.win}")
print(f"solution: {solution}")

mga.show_interpretable_genome(solution)

plt.plot([tournament for tournament in range(NUM_TOURNAMENTS)], mga.fitness_evolution_per_generation)
plt.show()
"""

# ---------------------------------------------------------------------
# Breath First-Search 

"""
# Environment
environment = Environment(width=WIDTH, height=HEIGHT, seed=SEED, difficulty=DIFFICULTY, agent_position_x=AGENT_POSITION_X, agent_position_y=AGENT_POSITION_Y, goal_position_x=GOAL_POSITION_X, goal_position_y=GOAL_POSITION_Y)
#environment.show_environment()

from solutions.uniformed_strategies import BFS
 
bfs = BFS(environment=environment, show_movements=True)
solution = bfs.solution()

if solution[0]:
    print(f"Goal found: {solution[0]} \nInitial Position: {solution[1]} \nFinal Position: {solution[2]}\n Steps Taken: {solution[3]}")
"""

# ---------------------------------------------------------------------
# Depth First-Search 

"""
# Environment
environment = Environment(width=WIDTH, height=HEIGHT, seed=SEED, difficulty=DIFFICULTY, agent_position_x=AGENT_POSITION_X, agent_position_y=AGENT_POSITION_Y, goal_position_x=GOAL_POSITION_X, goal_position_y=GOAL_POSITION_Y)
#environment.show_environment()

from solutions.uniformed_strategies import DFS
 
dfs = DFS(environment=environment, show_movements=True)
solution = dfs.solution()

if solution[0]:
    print(f"Goal found: {solution[0]} \nInitial Position: {solution[1]} \nFinal Position: {solution[2]}\nSteps Taken: {solution[3]}")
"""

# ---------------------------------------------------------------------
# DIJKSTRA (Uniform-Cost Search)

"""
# Environment
environment = Environment(width=WIDTH, height=HEIGHT, seed=SEED, difficulty=DIFFICULTY, agent_position_x=AGENT_POSITION_X, agent_position_y=AGENT_POSITION_Y, goal_position_x=GOAL_POSITION_X, goal_position_y=GOAL_POSITION_Y)
#environment.show_environment()

from solutions.uniformed_strategies import DIJKSTRA
 
dijkstra = DIJKSTRA(environment=environment, show_movements=True)
solution = dijkstra.solution()

if solution[0]:
    print(f"Goal found: {solution[0]} \nInitial Position: {solution[1]} \nFinal Position: {solution[2]}\nSteps taken: {solution[3]}")
"""

# ---------------------------------------------------------------------
# Iterative Deepening Search

"""
# Environment
environment = Environment(width=WIDTH, height=HEIGHT, seed=SEED, difficulty=DIFFICULTY, agent_position_x=AGENT_POSITION_X, agent_position_y=AGENT_POSITION_Y, goal_position_x=GOAL_POSITION_X, goal_position_y=GOAL_POSITION_Y)
#environment.show_environment()

from solutions.uniformed_strategies import IDS

ids = IDS(environment=environment, show_movements=True)
solution = ids.solution(max_depth=15)

print(solution)
"""

# ---------------------------------------------------------------------
# Greedy Best Search First

"""
# Environment
environment = Environment(width=WIDTH, height=HEIGHT, seed=SEED, difficulty=DIFFICULTY, agent_position_x=AGENT_POSITION_X, agent_position_y=AGENT_POSITION_Y, goal_position_x=GOAL_POSITION_X, goal_position_y=GOAL_POSITION_Y)
#environment.show_environment()

from solutions.informed_heuristics_strategies import GreedySearch

greedy = GreedySearch(environment=environment, show_movements=True)
solution = greedy.solution()

print(solution)
"""

# ---------------------------------------------------------------------
# A Start

"""
# Environment
environment = Environment(width=WIDTH, height=HEIGHT, seed=SEED, difficulty=DIFFICULTY, agent_position_x=AGENT_POSITION_X, agent_position_y=AGENT_POSITION_Y, goal_position_x=GOAL_POSITION_X, goal_position_y=GOAL_POSITION_Y)
#environment.show_environment()

from solutions.informed_heuristics_strategies import AStar

a_star = AStar(environment=environment, show_movements=True)
solution = a_star.solution()

print(solution)

"""

# ---------------------------------------------------------------------
# Iterative Deepening A Star (IDA)

"""
# Environment
environment = Environment(width=WIDTH, height=HEIGHT, seed=SEED, difficulty=DIFFICULTY, agent_position_x=AGENT_POSITION_X, agent_position_y=AGENT_POSITION_Y, goal_position_x=GOAL_POSITION_X, goal_position_y=GOAL_POSITION_Y)
#environment.show_environment()

from solutions.informed_heuristics_strategies import IDA

ida = IDA(environment=environment, show_movements=True)
solution = ida.solution()

print(f"Goal found: {solution[0]}\nSteps Taken: {solution[1]}\nGoal Coordenates: {solution[2]}\nExpanded Nodes: {ida.expanded_nodes}")
"""



# ---------------------------------------------------------------------
# Recursive Best-first Search (RBFS)

#"""
# Environment
environment = Environment(width=WIDTH, height=HEIGHT, seed=SEED, difficulty=DIFFICULTY, agent_position_x=AGENT_POSITION_X, agent_position_y=AGENT_POSITION_Y, goal_position_x=GOAL_POSITION_X, goal_position_y=GOAL_POSITION_Y)
#environment.show_environment()

from solutions.informed_heuristics_strategies import RBFS

rbfs = RBFS(environment=environment, show_movements=True)
solution = rbfs.solution()

if solution[0]:
    y_final, x_final = solution[1]
    print(f"Goal found: {True}\nGoal Coordenates: ({y_final}, {x_final})")
else:
    print(f"Goal found: {False}")
#"""

