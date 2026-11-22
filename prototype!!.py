
import random
cities = ["a", "b", "c", "d", "e"]

routes = {
    ("a", "b"): {"time": 4, "scenic": 6, "sleeper": 0, "changes": 1},
    ("a", "c"): {"time": 7, "scenic": 9, "sleeper": 1, "changes": 0},
    ("a", "d"): {"time": 6, "scenic": 5, "sleeper": 0, "changes": 2},
    ("a", "e"): {"time": 8, "scenic": 8, "sleeper": 1, "changes": 1},
    ("b", "c"): {"time": 5, "scenic": 4, "sleeper": 0, "changes": 1},
    ("b", "d"): {"time": 3, "scenic": 5, "sleeper": 0, "changes": 0},
    ("b", "e"): {"time": 6, "scenic": 7, "sleeper": 1, "changes": 1},
    ("c", "d"): {"time": 4, "scenic": 8, "sleeper": 0, "changes": 1},
    ("c", "e"): {"time": 5, "scenic": 9, "sleeper": 1, "changes": 0},
    ("d", "e"): {"time": 3, "scenic": 6, "sleeper": 0, "changes": 0},
}

def get_leg(city1, city2):
    if (city1, city2) in routes:
        return routes[(city1, city2)]
    elif (city2, city1) in routes:
        return routes[(city2, city1)]
    return None


def route_metrics(route):
    total_time = 0
    total_scenic = 0
    total_sleeper = 0
    total_changes = 0

    for i in range(len(route) - 1):
        leg = get_leg(route[i], route[i + 1])
        if leg is None:
            return None

        total_time += leg["time"]
        total_scenic += leg["scenic"]
        total_sleeper += leg["sleeper"]
        total_changes += leg["changes"]

    return {
        "time": total_time,
        "scenic": total_scenic,
        "sleeper": total_sleeper,
        "changes": total_changes
    }


def fitness(route, w_scenic=1.5, w_time=1.0, w_sleeper=2.0, w_changes=1.0):
    metrics = route_metrics(route)
    if metrics is None:
        return float("-inf")

    score = (
        w_scenic * metrics["scenic"]
        + w_sleeper * metrics["sleeper"]
        - w_time * metrics["time"]
        - w_changes * metrics["changes"]
    )
    return score

def make_population(size):
    population = []
    for x in range(size):
        cities_copy = cities[:]
        random.shuffle(cities_copy)
        population.append(cities_copy)
    return population

def select_parent(population):
    sample = random.sample(population, 3)
    sample.sort(key=fitness)
    return sample[-1]

def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [None]*len(parent1)

    child[start:end+1] = parent1[start:end+1]

    remainder = [x for x in parent2 if x not in child]

    rem_index = 0
    for x in range(len(child)):
        if child[x] is None:
            child[x] = remainder[rem_index]
            rem_index += 1

    return child

def mutate(route, mutation_rate=0.67):
    new_route = route[:]

    if random.random() < mutation_rate:
        pos1, pos2 = random.sample(range(len(route)), 2)
        new_route[pos1], new_route[pos2] = new_route[pos2], new_route[pos1]

    return new_route

def genetic_algorithm(pop_size=20, generations=50):
    population = make_population(pop_size)
    for x in range(generations):
        population.sort(key=fitness, reverse=True)
        best = population[0]
        print("Generation {}: {}, fitness = {}".format(x+1, best, fitness(best)))

        new_population = population[:2]

        while len(new_population) < pop_size:
            parent1 = select_parent(population)
            parent2 = select_parent(population)

            child = crossover(parent1,parent2)
            child = mutate(child)

            new_population.append(child)

        population = new_population

    population.sort(key=fitness, reverse=True)
    return population[0]

best = genetic_algorithm()
print("Best route found: {}".format(best))
print("Final fitness: {}".format(fitness(best)))


























