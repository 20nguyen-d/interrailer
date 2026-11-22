import csv
import random
import heapq
import matplotlib.pyplot as plt


class RouteSegment:
    def __init__(self, from_city, to_city, time_hours, scenic_score, changes):
        self.from_city = from_city
        self.to_city = to_city
        self.time_hours = float(time_hours)
        self.scenic_score = float(scenic_score)
        self.changes = int(changes)


class RailNetwork:
    def __init__(self):
        self.routes = {}
        self.graph = {}

    def add_route(self, segment):
        self._add_directed_route(segment)

        reverse_segment = RouteSegment(
            segment.to_city,
            segment.from_city,
            segment.time_hours,
            segment.scenic_score,
            segment.changes
        )

        self._add_directed_route(reverse_segment)

    def _add_directed_route(self, segment):
        self.routes[(segment.from_city, segment.to_city)] = segment

        if segment.from_city not in self.graph:
            self.graph[segment.from_city] = []

        self.graph[segment.from_city].append(segment.to_city)

    def load_from_csv(self, filename):
        with open(filename, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                segment = RouteSegment(
                    row["from_city"],
                    row["to_city"],
                    row["time_hours"],
                    row["scenic_score"],
                    row["changes"]
                )

                self.add_route(segment)

    def get_segment(self, from_city, to_city):
        return self.routes.get((from_city, to_city))

    def get_available_cities(self):
        cities = set()

        for from_city, to_city in self.routes:
            cities.add(from_city)
            cities.add(to_city)

        return sorted(cities)

    def shortest_path(self, start_city, end_city, time_weight, scenic_weight, changes_weight):
        priority_queue = []
        heapq.heappush(priority_queue, (0, start_city, [start_city]))

        best_known_costs = {start_city: 0}

        while priority_queue:
            current_cost, current_city, path = heapq.heappop(priority_queue)

            if current_city == end_city:
                return path

            for neighbour in self.graph.get(current_city, []):
                segment = self.get_segment(current_city, neighbour)

                edge_cost = (
                    time_weight * segment.time_hours
                    + changes_weight * segment.changes * 2
                    + scenic_weight * (10 - segment.scenic_score)
                )

                new_cost = current_cost + edge_cost

                if neighbour not in best_known_costs or new_cost < best_known_costs[neighbour]:
                    best_known_costs[neighbour] = new_cost
                    new_path = path + [neighbour]
                    heapq.heappush(priority_queue, (new_cost, neighbour, new_path))

        return None

    def calculate_path_stats(self, path):
        total_time = 0
        total_scenic = 0
        total_changes = 0

        for i in range(len(path) - 1):
            from_city = path[i]
            to_city = path[i + 1]

            segment = self.get_segment(from_city, to_city)

            total_time += segment.time_hours
            total_scenic += segment.scenic_score
            total_changes += segment.changes

        return {
            "time": total_time,
            "scenic": total_scenic,
            "changes": total_changes
        }


class GeneticAlgorithm:
    def __init__(
        self,
        rail_network,
        cities,
        start_city=None,
        end_city=None,
        population_size=80,
        generations=150,
        mutation_rate=0.15,
        time_weight=1.0,
        scenic_weight=0.0,
        changes_weight=1.0
    ):
        self.rail_network = rail_network
        self.cities = cities
        self.start_city = start_city
        self.end_city = end_city

        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate

        self.time_weight = time_weight
        self.scenic_weight = scenic_weight
        self.changes_weight = changes_weight

        self.best_scores = []
        self.mean_scores = []

    def get_middle_cities(self):
        middle_cities = self.cities[:]

        if self.start_city is not None:
            middle_cities.remove(self.start_city)

        if self.end_city is not None:
            middle_cities.remove(self.end_city)

        return middle_cities

    def rebuild_route(self, middle_cities):
        route = []

        if self.start_city is not None:
            route.append(self.start_city)

        route.extend(middle_cities)

        if self.end_city is not None:
            route.append(self.end_city)

        return route

    def create_individual(self):
        middle_cities = self.get_middle_cities()
        random.shuffle(middle_cities)
        return self.rebuild_route(middle_cities)

    def create_population(self):
        return [self.create_individual() for _ in range(self.population_size)]

    def calculate_route_stats(self, individual):
        total_time = 0
        total_scenic = 0
        total_changes = 0
        full_path = []

        for i in range(len(individual) - 1):
            start = individual[i]
            end = individual[i + 1]

            path = self.rail_network.shortest_path(
                start,
                end,
                self.time_weight,
                self.scenic_weight,
                self.changes_weight
            )

            if path is None:
                return None

            path_stats = self.rail_network.calculate_path_stats(path)

            listed_changes = path_stats["changes"]
            interchange_changes = max(0, len(path) - 2)

            total_time += path_stats["time"]
            total_scenic += path_stats["scenic"]
            total_changes += listed_changes + interchange_changes

            if len(full_path) == 0:
                full_path.extend(path)
            else:
                full_path.extend(path[1:])

        return {
            "time": total_time,
            "scenic": total_scenic,
            "changes": total_changes,
            "full_path": full_path
        }

    def fitness(self, individual):
        stats = self.calculate_route_stats(individual)

        if stats is None:
            return -999999

        score = (
            self.scenic_weight * stats["scenic"]
            - self.time_weight * stats["time"]
            - self.changes_weight * stats["changes"] * 2
        )

        return score

    def select_parent(self, population):
        tournament_size = min(5, len(population))
        tournament = random.sample(population, tournament_size)

        tournament.sort(
            key=lambda individual: self.fitness(individual),
            reverse=True
        )

        return tournament[0]

    def crossover(self, parent1, parent2):
        parent1_middle = self.extract_middle(parent1)
        parent2_middle = self.extract_middle(parent2)

        if len(parent1_middle) <= 1:
            return parent1[:]

        start = random.randint(0, len(parent1_middle) - 2)
        end = random.randint(start + 1, len(parent1_middle) - 1)

        middle_section = parent1_middle[start:end]

        child_middle = []

        for city in parent2_middle:
            if city not in middle_section:
                child_middle.append(city)

        child_middle[start:start] = middle_section

        return self.rebuild_route(child_middle)

    def extract_middle(self, route):
        middle = route[:]

        if self.start_city is not None:
            middle = middle[1:]

        if self.end_city is not None:
            middle = middle[:-1]

        return middle

    def mutate(self, individual):
        if random.random() < self.mutation_rate:
            middle = self.extract_middle(individual)

            if len(middle) <= 1:
                return individual

            index1, index2 = random.sample(range(len(middle)), 2)
            middle[index1], middle[index2] = middle[index2], middle[index1]

            return self.rebuild_route(middle)

        return individual

    def run(self):
        population = self.create_population()

        for generation in range(self.generations):
            population.sort(
                key=lambda individual: self.fitness(individual),
                reverse=True
            )

            scores = []

            for individual in population:
                score = self.fitness(individual)

                if score > -999999:
                    scores.append(score)

            if len(scores) == 0:
                best_score = -999999
                mean_score = -999999
            else:
                best_score = max(scores)
                mean_score = sum(scores) / len(scores)

            self.best_scores.append(best_score)
            self.mean_scores.append(mean_score)

            new_population = []

            new_population.append(population[0])

            if len(population) > 1:
                new_population.append(population[1])

            while len(new_population) < self.population_size:
                parent1 = self.select_parent(population)
                parent2 = self.select_parent(population)

                child = self.crossover(parent1, parent2)
                child = self.mutate(child)

                new_population.append(child)

            population = new_population

        population.sort(
            key=lambda individual: self.fitness(individual),
            reverse=True
        )

        best_route = population[0]
        best_stats = self.calculate_route_stats(best_route)
        best_score = self.fitness(best_route)

        return best_route, best_stats, best_score


def get_user_cities(network):
    available_cities = network.get_available_cities()

    print("\nAvailable cities in dataset:")
    print(", ".join(available_cities))

    while True:
        try:
            number_of_cities = int(input("\nHow many cities would you like to visit? "))

            if number_of_cities < 2:
                print("Please enter at least 2 cities.")
            elif number_of_cities > 20:
                print("Please enter no more than 20 cities.")
            elif number_of_cities > len(available_cities):
                print("There are not enough cities in the dataset.")
            else:
                break

        except ValueError:
            print("Please enter a whole number.")

    selected_cities = []

    while len(selected_cities) < number_of_cities:
        city = input(f"Enter city {len(selected_cities) + 1}: ").strip()

        if city not in available_cities:
            print("That city is not in the dataset. Please choose from the available cities.")
        elif city in selected_cities:
            print("You have already entered that city.")
        else:
            selected_cities.append(city)

    return selected_cities


def get_start_city(selected_cities):
    answer = input("\nWould you like to specify a start city? yes/no: ").strip().lower()

    if answer == "yes":
        while True:
            start_city = input("Enter start city: ").strip()

            if start_city in selected_cities:
                return start_city

            print("The start city must be one of your selected cities.")

    return None


def get_end_city(selected_cities, start_city):
    answer = input("\nWould you like to specify an end city? yes/no: ").strip().lower()

    if answer == "yes":
        while True:
            end_city = input("Enter end city: ").strip()

            if end_city not in selected_cities:
                print("The end city must be one of your selected cities.")
            elif end_city == start_city:
                print("The end city cannot be the same as the start city.")
            else:
                return end_city

    return None


def get_weight_profile():
    print("\nChoose a preference profile:")
    print("1. Fastest route")
    print("2. Scenic route")
    print("3. Fewest changes")
    print("4. Balanced route")
    print("5. Custom weights")

    while True:
        choice = input("Enter profile number: ").strip()

        if choice == "1":
            print("\nProfile selected: Fastest route")
            return 2.5, 0.0, 1.0

        elif choice == "2":
            print("\nProfile selected: Scenic route")
            return 0.8, 2.5, 0.8

        elif choice == "3":
            print("\nProfile selected: Fewest changes")
            return 1.0, 0.0, 3.0

        elif choice == "4":
            print("\nProfile selected: Balanced route")
            return 1.0, 1.0, 1.0

        elif choice == "5":
            print("\nCustom weights selected.")
            return get_custom_weights()

        else:
            print("Please enter a number from 1 to 5.")


def get_custom_weights():
    print("\nEnter custom preference weights.")
    print("Higher values mean that factor is more important.")
    print("If scenic scores are not filled in yet, enter 0 for scenic value.")

    while True:
        try:
            time_weight = float(input("Importance of reducing travel time: "))
            scenic_weight = float(input("Importance of scenic value: "))
            changes_weight = float(input("Importance of reducing changes: "))

            if time_weight < 0 or scenic_weight < 0 or changes_weight < 0:
                print("Weights cannot be negative.")
            else:
                return time_weight, scenic_weight, changes_weight

        except ValueError:
            print("Please enter numbers only.")


def print_route_result(network, selected_visit_order, stats, score):
    print("\nSelected City Visit Order:")
    print(" -> ".join(selected_visit_order))

    print("\nFull Rail Path Including Interchange Cities:")
    print(" -> ".join(stats["full_path"]))

    print("\nJourney Statistics:")
    print(f"Total travel time: {round(stats['time'], 2)} hours")
    print(f"Total scenic score: {round(stats['scenic'], 2)}")
    print(f"Total changes: {stats['changes']}")
    print(f"Fitness score: {round(score, 2)}")

    print("\nDetailed Rail Legs:")

    full_path = stats["full_path"]

    for i in range(len(full_path) - 1):
        from_city = full_path[i]
        to_city = full_path[i + 1]
        segment = network.get_segment(from_city, to_city)

        print(f"\nLeg {i + 1}: {from_city} to {to_city}")
        print(f"Time: {segment.time_hours} hours")
        print(f"Scenic score: {segment.scenic_score}/10")
        print(f"Changes listed for this rail segment: {segment.changes}")

    print("\nLong Leg Notes:")

    found_long_leg = False

    for i in range(len(full_path) - 1):
        from_city = full_path[i]
        to_city = full_path[i + 1]
        segment = network.get_segment(from_city, to_city)

        if segment.time_hours >= 7:
            found_long_leg = True
            print(
                f"- {from_city} to {to_city} is {segment.time_hours} hours. "
                f"Consider checking whether an overnight train is available or breaking the journey."
            )

    if not found_long_leg:
        print("No individual rail leg is over 7 hours.")


def plot_route_summary(stats):
    labels = ["Total time", "Scenic score", "Changes"]
    values = [
        stats["time"],
        stats["scenic"],
        stats["changes"]
    ]

    plt.figure()
    plt.bar(labels, values)
    plt.title("Optimised Journey Summary")
    plt.ylabel("Value")


def plot_ga_analysis(ga):
    plt.figure()
    plt.plot(ga.best_scores, label="Best GA fitness score")
    plt.plot(ga.mean_scores, label="Mean GA fitness score")
    plt.xlabel("Generation")
    plt.ylabel("Fitness score")
    plt.title("Genetic Algorithm Performance Over Time")
    plt.legend()


def greedy_baseline(network, selected_cities, start_city, end_city, time_weight, scenic_weight, changes_weight):
    unvisited = selected_cities[:]

    if start_city is not None:
        current_city = start_city
        unvisited.remove(start_city)
    else:
        current_city = unvisited.pop(0)

    if end_city is not None and end_city in unvisited:
        unvisited.remove(end_city)

    route = [current_city]

    while unvisited:
        best_city = None
        best_cost = float("inf")

        for city in unvisited:
            path = network.shortest_path(
                current_city,
                city,
                time_weight,
                scenic_weight,
                changes_weight
            )

            if path is not None:
                stats = network.calculate_path_stats(path)

                interchange_changes = max(0, len(path) - 2)

                cost = (
                    time_weight * stats["time"]
                    + changes_weight * (stats["changes"] + interchange_changes) * 2
                    + scenic_weight * (10 * (len(path) - 1) - stats["scenic"])
                )

                if cost < best_cost:
                    best_cost = cost
                    best_city = city

        if best_city is None:
            break

        route.append(best_city)
        unvisited.remove(best_city)
        current_city = best_city

    if end_city is not None:
        route.append(end_city)

    return route


def main():
    network = RailNetwork()
    network.load_from_csv("routes.csv")

    selected_cities = get_user_cities(network)
    start_city = get_start_city(selected_cities)
    end_city = get_end_city(selected_cities, start_city)

    time_weight, scenic_weight, changes_weight = get_weight_profile()

    ga = GeneticAlgorithm(
        rail_network=network,
        cities=selected_cities,
        start_city=start_city,
        end_city=end_city,
        population_size=80,
        generations=150,
        mutation_rate=0.15,
        time_weight=time_weight,
        scenic_weight=scenic_weight,
        changes_weight=changes_weight
    )

    best_route, best_stats, best_score = ga.run()

    if best_stats is None:
        print("\nNo valid route could be found using the current dataset.")
        return

    print_route_result(network, best_route, best_stats, best_score)

    greedy_route = greedy_baseline(
        network,
        selected_cities,
        start_city,
        end_city,
        time_weight,
        scenic_weight,
        changes_weight
    )

    greedy_stats = ga.calculate_route_stats(greedy_route)
    greedy_score = ga.fitness(greedy_route)

    print("\nGreedy Baseline Selected City Visit Order:")
    print(" -> ".join(greedy_route))

    if greedy_stats is not None:
        print("\nGreedy Baseline Full Rail Path Including Interchange Cities:")
        print(" -> ".join(greedy_stats["full_path"]))

        print("\nComparison:")
        print(f"GA fitness score: {round(best_score, 2)}")
        print(f"Greedy baseline fitness score: {round(greedy_score, 2)}")

        if best_score > greedy_score:
            print("The genetic algorithm found a better route than the greedy baseline.")
        elif best_score == greedy_score:
            print("The genetic algorithm matched the greedy baseline.")
        else:
            print("The greedy baseline performed better for this particular run.")
    else:
        print("The greedy baseline could not produce a valid route.")

    plot_route_summary(best_stats)
    plot_ga_analysis(ga)

    plt.show()


if __name__ == "__main__":
    main()