class GeneticAlgorithm:
    def __init__(
        self, 
        generate_random_specimen,
        fitness,
        selection,
        mutation,
        mutation_rate,
        crossover,
        goal = None,
        generations = 10,
        initial_population_size = 10
        ):
        self.population = [generate_random_specimen() for i in range(initial_population_size)]
        self.fitness = fitness
        self.generations = generations
        self.best_performers = []
        self.crossover = crossover
        self.selection = selection
        self.mutation = mutation
        self.mutation_rate = mutation_rate
        self.goal = goal
    
    def run(self):
        best_performers = []
        for generation in range(self.generations):
            fitnesses = [self.fitness(specimen) for specimen in self.population]
            best_individual = max(self.population, key=self.fitness)
            best_fitness = self.fitness(best_individual)
            best_performers.append((best_individual, best_fitness))
            if best_individual == self.goal:
                break
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