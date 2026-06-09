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

# Environment
environment = Environment(width=WIDTH, height=HEIGHT, seed=SEED, difficulty=DIFFICULTY, agent_position_x=AGENT_POSITION_X, agent_position_y=AGENT_POSITION_Y, goal_position_x=GOAL_POSITION_X, goal_position_y=GOAL_POSITION_Y)
#environment.show_environment()


# ---------------------------------------------------------------------
# Simple Genetic Algorithm
# Global variables
MUTATION_RATE = 0.05
POP_SIZE = 100
NUM_GENES = 20
NUM_GENERATIONS = 500

"""
# Simple Genetic Algorithm
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
from solutions.uniformed_strategies import BFS
 
bfs = BFS(environment=environment, show_movements=True)
solution = bfs.solution()

if solution[0]:
    print(f"Goal found: {solution[0]} \nInitial Position: {solution[1]} \nFinal Position: {solution[2]}")
"""

# ---------------------------------------------------------------------
# Depth First-Search 

"""
from solutions.uniformed_strategies import DFS
 
dfs = DFS(environment=environment, show_movements=True)
solution = dfs.solution()

if solution[0]:
    print(f"Goal found: {solution[0]} \nInitial Position: {solution[1]} \nFinal Position: {solution[2]}")
"""

# ---------------------------------------------------------------------
# DIJKSTRA (Uniform-Cost Search)

"""
from solutions.uniformed_strategies import DIJKSTRA
 
dijkstra = DIJKSTRA(environment=environment, show_movements=True)
solution = dijkstra.solution()

if solution[0]:
    print(f"Goal found: {solution[0]} \nInitial Position: {solution[1]} \nFinal Position: {solution[2]}")
"""

# ---------------------------------------------------------------------
# DIJKSTRA (Uniform-Cost Search)

#"""
from solutions.uniformed_strategies import IDS

ids = IDS(environment=environment, show_movements=True)
solution = ids.solution(max_depth=15)

print(solution)
#"""