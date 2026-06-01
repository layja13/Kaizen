import random

class  SimpleGeneticAlgorithm:
    def __init__(self, environment, mutation_rate, pop_size, num_generations, num_genes):
        self.environment = environment
        self.agent_position_y = self.environment.agent_position_y
        self.agent_position_x = self.environment.agent_position_x
        self.mutation_rate = mutation_rate
        self.pop_size = pop_size
        self.num_generations = num_generations
        self.num_genes = num_genes
        self.win = False
        self.actions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        self.actions_interpretable = {(-1, 0):"UP", (1, 0):"DOWN", (0, 1):"RIGHT", (0, -1):"LEFT"}
        self.population = self._create_population()
        self.population_fitness = self._create_population_fitness()
        self.fitness_evolution_per_generation = []


    def _create_population(self):
        return [[random.choice(self.actions) for gen in range(self.num_genes)] for candidate in range(self.pop_size)]


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


    def _create_population_fitness(self):
        poblation_fitness = []

        for candidate in self.population:
            poblation_fitness.append(self._evaluate_candidate(candidate))

            self.agent_position_y = self.environment.agent_position_y
            self.agent_position_x = self.environment.agent_position_x
            
        return poblation_fitness
            
    
    def evolve(self):
        best_fitness = float("-inf")
        best_candidate = None


        for generation in range(self.num_generations):
            new_generation = []

            # Tracking the best fitnesses per generation
            best_fitness_generation = max(self.population_fitness)
            self.fitness_evolution_per_generation.append(best_fitness_generation)

            # Tracking the best candidate
            if best_fitness_generation > best_fitness:
                best_fitness = best_fitness_generation
                best_candidate_index = self.population_fitness.index(best_fitness_generation)

                best_candidate = self.population[best_candidate_index]


            for candidate in range(self.pop_size):
                # Selection
                parent_one = self._selection_tournament(num_candidates=2)
                parent_two = self._selection_tournament(num_candidates=2)

                # Cross-over
                child = self._cross_over(parent_one, parent_two)
                
                # Mutation
                child_mutated = self._mutation(child)

                new_generation.append(child_mutated)

            self.population = new_generation
            self.population_fitness = self._create_population_fitness()
        
        return best_candidate



    def _selection_tournament(self, num_candidates=2):
        indexes = []
        for i in range(num_candidates):
            indexes.append(random.randint(0, self.pop_size - 1))
        
        max_fitness = float("-inf")
        max_index = float("-inf")

        for index in indexes:
            fitness = self.population_fitness[index]
            if fitness > max_fitness:
                max_fitness = fitness
                max_index = index

        return self.population[max_index]


    def _cross_over(self, parent_one, parent_two):
        # Half of one parent and half of the other one
        return parent_one[:len(parent_one)//2] + parent_two[len(parent_two)//2:]
    

    def _mutation(self, child):
        child_copy = child.copy()
        
        for gen in range(len(child)):
            if random.random() < self.mutation_rate:
                
                new_gen = random.choice(self.actions)
                while new_gen == child_copy[gen]:
                    new_gen = random.choice(self.actions)

                child_copy[gen] = new_gen

        return child_copy


    def _fitness(self, steps, min_distance, win):
        area = self.environment.height*self.environment.width
        if win:
            return area - steps
        elif win == False:
            return -area -min_distance
        else:
            return -min_distance
        
    
    def _evaluate_candidate(self, candidate):
        steps = 0
        minimum_distance = self._manhattan_distance()

        for gen in candidate:
            self._move(gen)
            steps += 1
            minimum_distance = min(minimum_distance, self._manhattan_distance())

            if self._game_on() == False:
                return self._fitness(steps=steps, min_distance=minimum_distance, win=False)
            elif self.environment.environment[self.agent_position_y][self.agent_position_x] == "G":
                self.win = True
                return self._fitness(steps=steps, min_distance=minimum_distance, win=True)
            
        return self._fitness(steps=steps, min_distance=minimum_distance, win=None)


    
    def _move(self, gen):
        dy = gen[0]
        dx = gen[1]

        self.agent_position_y += dy
        self.agent_position_x += dx
        return
    

    def _game_on(self):
        if self.agent_position_y < 0 or self.agent_position_x < 0 or self.agent_position_y > self.environment.height - 1 \
            or self.agent_position_x > self.environment.width - 1 or self.environment.environment[self.agent_position_y][self.agent_position_x] == "O":
            return False
        return True
    
    
    def _manhattan_distance(self):
        return abs(self.environment.goal_position_y - self.agent_position_y) + abs(self.environment.goal_position_x - self.agent_position_x)
    
