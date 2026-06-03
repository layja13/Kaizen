from maze_solver import MazeSolverBase
import random


class GeneticAlgorithmBase(MazeSolverBase):
    def __init__(self, environment, mutation_rate, pop_size, num_genes):
        super().__init__(environment)
        self.mutation_rate = mutation_rate
        self.pop_size = pop_size
        self.num_genes = num_genes
        self.win = False
        self.fitness_evolution_per_generation = []
        self.reset_agent_position()
        self.population = self._create_population()
        self.population_fitness = self._create_population_fitness()


    def _create_population(self):
        return [
            [random.choice(self.actions) for gen in range(self.num_genes)]
            for candidate in range(self.pop_size)
        ]


    def _create_population_fitness(self):
        population_fitness = []
        self.population_steps = []

        for candidate in self.population:
            fitness, steps = self._evaluate_candidate(candidate)

            population_fitness.append(fitness)
            self.population_steps.append(steps)

            self.reset_agent_position()

        return population_fitness


    def _selection_tournament(self, num_candidates=2):
        indexes = []
        for i in range(num_candidates):
            indexes.append(random.randint(0, self.pop_size - 1))

        max_fitness = float("-inf")
        max_index = None

        for index in indexes:
            fitness = self.population_fitness[index]
            if fitness > max_fitness:
                max_fitness = fitness
                max_index = index

        return self.population[max_index], max_index


    def _mutation(self, child):
        child_copy = child.copy()

        for gen in range(len(child_copy)):
            if random.random() < self.mutation_rate:
                new_gen = random.choice(self.actions)

                while new_gen == child_copy[gen]:
                    new_gen = random.choice(self.actions)

                child_copy[gen] = new_gen

        return child_copy


    def _fitness(self, steps, min_distance, win):
        area = self.environment.height * self.environment.width

        if win:
            return area - steps
        elif win == False:
            return -area - min_distance
        else:
            return -min_distance


    def _evaluate_candidate(self, candidate):
        steps = 0
        minimum_distance = self.manhattan_distance()

        for gen in candidate:
            self.move(gen)
            steps += 1
            minimum_distance = min(minimum_distance, self.manhattan_distance())

            if self.game_on() == False:
                return self._fitness(steps=steps, min_distance=minimum_distance, win=False), steps
            elif self.environment.environment[self.agent_position_y][self.agent_position_x] == "G":
                self.win = True
                return self._fitness(steps=steps, min_distance=minimum_distance, win=True), steps

        return self._fitness(steps=steps, min_distance=minimum_distance, win=None), steps


    def show_population(self, interpretable=False):
        if interpretable:
            for candidate in self.population:
                complete_interpretable_candidate = []

                for gen in candidate:
                    complete_interpretable_candidate.append(self.actions_interpretable[gen])

                print(complete_interpretable_candidate)
        else:
            for candidate in self.population:
                print(candidate)


    def show_interpretable_genome(self, genome):
        genome_interpretable = []

        for gen in genome:
            genome_interpretable.append(self.actions_interpretable[gen])

        print(genome_interpretable)


# ---------------------------------------------------------------------------------
class SimpleGeneticAlgorithm(GeneticAlgorithmBase):
    def __init__(self, environment, mutation_rate, pop_size, num_generations, num_genes):
        self.num_generations = num_generations
        super().__init__(
            environment=environment,
            mutation_rate=mutation_rate,
            pop_size=pop_size,
            num_genes=num_genes,
        )


    def evolve(self):
        best_fitness = float("-inf")
        best_candidate = None

        for generation in range(self.num_generations):
            best_fitness, best_candidate = self._update_best_candidate(
                best_fitness=best_fitness,
                best_candidate=best_candidate,
                track_fitness=True,
            )

            new_generation = []

            for candidate in range(self.pop_size):
                parent_one, _ = self._selection_tournament(num_candidates=2)
                parent_two, _ = self._selection_tournament(num_candidates=2)

                child = self._cross_over(parent_one, parent_two)
                child_mutated = self._mutation(child)

                new_generation.append(child_mutated)

            self.population = new_generation
            self.population_fitness = self._create_population_fitness()


        best_fitness, best_candidate = self._update_best_candidate(
            best_fitness=best_fitness,
            best_candidate=best_candidate,
            track_fitness=False,
        )

        return best_candidate


    def _update_best_candidate(self, best_fitness, best_candidate, track_fitness):
        best_fitness_generation = max(self.population_fitness)

        if track_fitness:
            self.fitness_evolution_per_generation.append(best_fitness_generation)

        if best_fitness_generation > best_fitness:
            best_fitness = best_fitness_generation
            best_candidate_index = self.population_fitness.index(best_fitness_generation)
            best_steps = self.population_steps[best_candidate_index]
            best_candidate = self.population[best_candidate_index][:best_steps]

        return best_fitness, best_candidate


    def _cross_over(self, parent_one, parent_two):
        return parent_one[: len(parent_one) // 2] + parent_two[len(parent_two) // 2 :]


class MicrobialGeneticAlgorithm(GeneticAlgorithmBase):
    def __init__(self, environment, mutation_rate, pop_size, num_genes, num_tournaments, sharing_genes_rate):
        self.num_tournaments = num_tournaments
        self.sharing_genes_rate = sharing_genes_rate
        super().__init__(
            environment=environment,
            mutation_rate=mutation_rate,
            pop_size=pop_size,
            num_genes=num_genes,
        )

    def evolve(self):
        highest_fitness = max(self.population_fitness)
        best_candidate_index = self.population_fitness.index(highest_fitness)
        best_steps = self.population_steps[best_candidate_index]
        best_candidate = self.population[best_candidate_index][:best_steps]

        for tournament in range(self.num_tournaments):
            parent_one, index_parent_one = self._selection_tournament(num_candidates=2)
            parent_two, index_parent_two = self._selection_tournament(num_candidates=2)

            new_candidate = self._cross_over(
                parent_one=parent_one,
                parent_two=parent_two,
                index_parent_one=index_parent_one,
                index_parent_two=index_parent_two,
            )

            new_candidate_mutated = self._mutation(new_candidate)

            fitness, steps = self._evaluate_candidate(new_candidate_mutated)
            self.reset_agent_position()

            if self.population_fitness[index_parent_one] > self.population_fitness[index_parent_two]:
                replacement_index = index_parent_two
            else:
                replacement_index = index_parent_one

            self.population[replacement_index] = new_candidate_mutated
            self.population_fitness[replacement_index] = fitness
            self.population_steps[replacement_index] = steps

            if fitness > highest_fitness:
                highest_fitness = fitness
                best_candidate = new_candidate_mutated[:steps]

            self.fitness_evolution_per_generation.append(highest_fitness)

        return best_candidate


    def _cross_over(self, parent_one, parent_two, index_parent_one, index_parent_two):
        if self.population_fitness[index_parent_one] > self.population_fitness[index_parent_two]:
            winner = parent_one
            loser = parent_two
        else:
            winner = parent_two
            loser = parent_one

        child = loser.copy()

        for gen in range(len(child)):
            if random.random() < self.sharing_genes_rate:
                child[gen] = winner[gen]

        return child
