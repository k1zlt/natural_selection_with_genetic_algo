# 1. Initialization: Create a random population of chromosomes.
# 2. Fitness Evaluation: Evaluate the fitness of each chromosome.
# 3. Selection: Select parent chromosomes based on fitness.
# 4. Crossover: Recombine parents to produce offspring.
# 5. Mutation: Apply random mutations to some offspring.
# 6. Replacement: Form a new population with the offspring.
# 7. Termination: Repeat until a stopping condition is met.
# 8. Result: Return the best solution found.

class GeneticAlgorithm:
    def __init__(
        self, 
        generate_random_specimen,
        fitness,
        selection,
        mutation,
        mutation_rate,
        crossover,
        generations = 10,
        initial_population_size = 10
        ):
        self.population = [generate_random_specimen() for i in range(initial_population_size)]
        self.fitness = fitness
        self.generations = generations
        self.best_performers = []
        self.all_populations = []
        self.crossover = crossover
        self.selection = selection
        self.mutation = mutation
        self.mutation_rate = mutation_rate
    
    def run(self):
        best_performers = []
        for generation in range(self.generations):
            fitnesses = [self.fitness(specimen) for specimen in self.population]
            best_individual = max(self.population, key=self.fitness)
            best_fitness = self.fitness(best_individual)
            best_performers.append((best_individual, best_fitness))
            self.all_populations.append(self.population[:])
            self.population = self.selection(self.population, fitnesses)
            next_population = []
            for i in range(0, len(self.population) // 2):
                parent1 = self.population[2*i]
                parent2 = self.population[2*i+1]
                child1, child2 = self.crossover(parent1, parent2)
                next_population.append(self.mutation(child1, self.mutation_rate))
                next_population.append(self.mutation(child2, self.mutation_rate))
            next_population.append(best_individual)
            self.population = next_population
        return best_performers
            
                        