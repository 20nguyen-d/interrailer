import random
import heapq
import matplotlib.pyplot as plt

cities = ["London", "Paris", "Brussels", "Amsterdam", "Berlin", "Prague"]

routes = {
    ("London", "Paris"): {"time": 136, "scenic": 5, "sleeper": 0, "changes": 0},
    ("London", "Brussels"): {"time": 113, "scenic": 5, "sleeper": 0, "changes": 0},
    ("London", "Amsterdam"): {"time": 259, "scenic": 5, "sleeper": 0, "changes": 0},
    ("Paris", "Brussels"): {"time": 82, "scenic": 5, "sleeper": 0, "changes": 0},
    ("Brussels", "Amsterdam"): {"time": 128, "scenic": 5, "sleeper": 0, "changes": 0},
    ("Paris", "Berlin"): {"time": 901, "scenic": 5, "sleeper": 1, "changes": 0},
    ("Brussels", "Berlin"): {"time": 684, "scenic": 5, "sleeper": 1, "changes": 0},
    ("Brussels", "Prague"): {"time": 929, "scenic": 5, "sleeper": 1, "changes": 0},
    ("Amsterdam", "Berlin"): {"time": 474, "scenic": 5, "sleeper": 1, "changes": 0},
    ("Berlin", "Prague"): {"time": 280, "scenic": 5, "sleeper": 0, "changes": 0},
}

def normalize(value, min_value, max_value):
    if max_value == min_value:
        return 0
    return (value - min_value) / (max_value - min_value)


def sleeper_leg_score(leg, threshold=360):
    if leg["time"] <= threshold:
        return 1
    if leg["sleeper"] == 1:
        return 1
    return 0


def path_metrics(path, graph):
    total_time = 0
    total_scenic = 0
    total_sleeper_score = 0

    for i in range(len(path) - 1):
        leg = graph[path[i]][path[i + 1]]

        total_time += leg["time"]
        total_scenic += leg["scenic"]
        total_sleeper_score += sleeper_leg_score(leg)

    return {
        "time": total_time,
        "scenic": total_scenic,
        "sleeper_score": total_sleeper_score
    }


def route_metrics(route, graph):
    total_time = 0
    total_scenic = 0
    total_sleeper_score = 0
    full_path = [route[0]]

    for i in range(len(route) - 1):
        start = route[i]
        end = route[i + 1]

        best_path, _ = shortest_path(graph, start, end)
        if best_path is None:
            return None

        metrics = path_metrics(best_path, graph)

        total_time += metrics["time"]
        total_scenic += metrics["scenic"]
        total_sleeper_score += metrics["sleeper_score"]

        full_path.extend(best_path[1:])

    return {
        "time": total_time,
        "scenic": total_scenic,
        "sleeper_score": total_sleeper_score,
        "num_legs": len(full_path) - 1,
        "full_path": full_path
    }


def dataset_bounds(routes):
    times = []
    scenics = []

    for leg_data in routes.values():
        times.append(leg_data["time"])
        scenics.append(leg_data["scenic"])

    return {
        "time_min": min(times),
        "time_max": max(times),
        "scenic_min": min(scenics),
        "scenic_max": max(scenics)
    }


def normalize_metrics(metrics, bounds):
    num_legs = metrics["num_legs"]

    time_min_total = num_legs * bounds["time_min"]
    time_max_total = num_legs * bounds["time_max"]

    scenic_min_total = num_legs * bounds["scenic_min"]
    scenic_max_total = num_legs * bounds["scenic_max"]

    sleeper_min_total = 0
    sleeper_max_total = num_legs

    norm_time = 1 - normalize(metrics["time"], time_min_total, time_max_total)
    norm_scenic = normalize(metrics["scenic"], scenic_min_total, scenic_max_total)
    norm_sleeper = normalize(metrics["sleeper_score"], sleeper_min_total, sleeper_max_total)

    return {
        "time": norm_time,
        "scenic": norm_scenic,
        "sleeper": norm_sleeper
    }


def fitness(route, graph, bounds, w_time=1.0, w_scenic=1.0, w_sleeper=1.0):
    metrics = route_metrics(route, graph)
    if metrics is None:
        return float("-inf")

    norm = normalize_metrics(metrics, bounds)

    return (
        w_time * norm["time"]
        + w_scenic * norm["scenic"]
        + w_sleeper * norm["sleeper"]
    )
def build_graph(routes):
    graph = {}

    for (city1, city2), data in routes.items():
        if city1 not in graph:
            graph[city1] = {}
        if city2 not in graph:
            graph[city2] = {}

        graph[city1][city2] = data
        graph[city2][city1] = data

    return graph


def shortest_path(graph, start, end):
    priority_queue = [(0, start, [start])]
    visited = set()

    while priority_queue:
        current_cost, current_city, path_so_far = heapq.heappop(priority_queue)

        if current_city in visited:
            continue

        visited.add(current_city)

        if current_city == end:
            return path_so_far, current_cost

        for neighbour, edge_data in graph[current_city].items():
            if neighbour not in visited:
                new_cost = current_cost + edge_data["time"]
                new_path = path_so_far + [neighbour]
                heapq.heappush(priority_queue, (new_cost, neighbour, new_path))

    return None, float("inf")





def make_individual(city_list):
    route = city_list[:]
    random.shuffle(route)
    return route


def make_population(city_list, size):
    return [make_individual(city_list) for _ in range(size)]


def select_parent(population, graph, bounds, w_time, w_scenic, w_sleeper):
    sample = random.sample(population, 3)
    sample.sort(
        key=lambda route: fitness(route, graph, bounds, w_time, w_scenic, w_sleeper),
        reverse=True
    )
    return sample[0]


def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [None] * len(parent1)

    child[start:end+1] = parent1[start:end+1]
    remaining = [city for city in parent2 if city not in child]

    index = 0
    for i in range(len(child)):
        if child[i] is None:
            child[i] = remaining[index]
            index += 1

    return child


def mutate(route, mutation_rate=0.1):
    new_route = route[:]
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(route)), 2)
        new_route[i], new_route[j] = new_route[j], new_route[i]
    return new_route


def format_route(route):
    return " -> ".join(route)


def genetic_algorithm(
    city_list,
    graph,
    bounds,
    pop_size=20,
    generations=20,
    mutation_rate=0.1,
    w_time=1.0,
    w_scenic=1.5,
    w_sleeper=2.0
):
    population = make_population(city_list, pop_size)
    best_history = []
    avg_history = []

    for gen in range(generations):
        population.sort(
            key=lambda route: fitness(route, graph, bounds, w_time, w_scenic, w_sleeper),
            reverse=True
        )

        best = population[0]
        best_score = fitness(best, graph, bounds, w_time, w_scenic, w_sleeper)

        avg_score = sum(
            fitness(route, graph, bounds, w_time, w_scenic, w_sleeper)
            for route in population
        ) / len(population)

        best_history.append(best_score)
        avg_history.append(avg_score)

        best_metrics = route_metrics(best, graph)

        print("Generation number {}".format(gen+1))
        print("  Target route :", format_route(best))

        print("  Full path    :", format_route(best_metrics["full_path"]))
        print("  Best fitness :", round(best_score, 2))
        print("  Stats      :", best_metrics)
        print("  Average fit :", round(avg_score, 2))
        print()

        new_population = population[:2]

        while len(new_population) < pop_size:
            parent1 = select_parent(population, graph, bounds, w_time, w_scenic, w_sleeper)
            parent2 = select_parent(population, graph, bounds, w_time, w_scenic, w_sleeper)

            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)

            new_population.append(child)

        population = new_population

    population.sort(
        key=lambda route: fitness(route, graph, bounds, w_time, w_scenic, w_sleeper),
        reverse=True
    )

    best = population[0]
    best_metrics = route_metrics(best, graph)
    best_score = fitness(best, graph, bounds, w_time, w_scenic, w_sleeper)

    return best, best_score, best_metrics, best_history, avg_history


def plot_fitness(best_history, avg_history):
    generations = list(range(1, len(best_history) + 1))
    plt.plot(generations, best_history, label="Best fitness")
    plt.plot(generations, avg_history, label="Average fitness")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.title("Fitness over generations")
    plt.legend()
    plt.show()


graph = build_graph(routes)
bounds = dataset_bounds(routes)
best_route, best_score, best_metrics, best_history, avg_history = genetic_algorithm(
    cities,
    graph,
    bounds,
    pop_size=20,
    generations=20,
    mutation_rate=0.1,
    w_time=1.0,
    w_scenic=2.0,
    w_sleeper=2.0
)

print("FINAL RESULT !")
print("Target route:", format_route(best_route))
print("Full path:", format_route(best_metrics["full_path"]))
print("Best fitness:", round(best_score, 2))
print("Stats:", best_metrics)

plot_fitness(best_history, avg_history)











































