from GeneticAlgorithm import GeneticAlgorithm
import random

def get_dna(specimen):
    v = []
    while specimen > 0:
        v.append(specimen % 2)
        specimen //= 2
    while len(v) < 15:
        v.append(0)
    return v[::-1]

def get_specimen(dna):
    s = 0
    k = 0
    for i in range(len(dna) - 1, -1, -1):
        s += dna[i] * 2 ** k
        k += 1
    return s

def generate_random_specimen():
    return random.choice(range(0, 3))

def fitness_function(specimen):
    return specimen ** 2

def selection(population, fitnesses, size = 3):
    selected = []
    for i in range(len(population)):
        tournament = random.sample(list(zip(population, fitnesses)), size)
        winner = max(tournament, key = lambda x: x[1])[0]
        selected.append(winner)
    return selected

def crossover(parent1, parent2):
    dna1 = get_dna(parent1)
    dna2 = get_dna(parent2)
    child1 = []
    child2 = []
    for i in range(len(dna1)):
        if random.choice(range(2)) == 1:
            child1.append(dna1[i])
            child2.append(dna2[i])
        else:
            child1.append(dna2[i])
            child2.append(dna1[i])
    return get_specimen(child1), get_specimen(child2)

def mutation(specimen, mutation_rate):
    specimen = get_dna(specimen)
    if random.random() < mutation_rate:
        i = random.choice(range(len(specimen)))
        specimen[i] = (specimen[i] + 1) % 2
    return get_specimen(specimen)

if __name__ == "__main__":
    GenAlgo = GeneticAlgorithm(
        generate_random_specimen = generate_random_specimen,
        fitness = fitness_function,
        selection = selection,
        mutation = mutation,
        crossover = crossover,
        goal = 2 ** 15 - 1,
        mutation_rate = 0.1,
        generations = 100,
        initial_population_size = 10
    )
    
    for index, i in enumerate(GenAlgo.run()):
        dna = get_dna(i[0])
        print(index, i[0], dna, i[1], sum(dna)/len(dna))
