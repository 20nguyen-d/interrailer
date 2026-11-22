import csv
import random
import heapq
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt



# data classes

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
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)

            required_columns = {
                "from_city",
                "to_city",
                "time_hours",
                "scenic_score",
                "changes"
            }

            if not required_columns.issubset(reader.fieldnames):
                raise ValueError(
                    "CSV must contain: from_city, to_city, time_hours, scenic_score, changes"
                )

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
            segment = self.get_segment(path[i], path[i + 1])

            total_time += segment.time_hours
            total_scenic += segment.scenic_score
            total_changes += segment.changes

        return {
            "time": total_time,
            "scenic": total_scenic,
            "changes": total_changes
        }



# Genetic algorithm


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

    def extract_middle(self, route):
        middle = route[:]

        if self.start_city is not None:
            middle = middle[1:]

        if self.end_city is not None:
            middle = middle[:-1]

        return middle

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

            # Elitism
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



# greedy baseline


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



# GUI start
# theme colours
CURRENT_THEME = "navy_modern"
THEMES = {

    "navy_modern": {
        "background": "#0f172a",
        "surface": "#1e293b",
        "surface_alt": "#334155",
        "text": "#f8faFC",
        "muted": "#cbd5e1",
        "heading": "#f8fafc",
        "accent": "#38bdf8",
        "accent_hover": "#7dd3fc",
        "accent_text": "#082f49",
        "danger": "#fb7185",
        "danger_hover": "#f43f5e",
        "danger_text": "#0f172a",
        "success": "#22c55e",
        "success_hover": "#16a34a",
        "success_text": "#052e16",
        "info": "#bae6fd",
        "info_hover": "#7dd3fc",
        "info_text": "#082f49",
        "border": "#38bdF8",
        "entry_bg": "#334155",
        "selection_bg": "#38bdF8",
        "selection_text": "#082f49",
    },

    "vintage_rail": {
        "background": "#3e2f26",
        "surface": "#f3e1b6",
        "surface_alt": "#e5c98f",
        "text": "#3e2f26",
        "muted": "#725f4a",
        "heading": "#8c2f24",
        "accent": "#c9822b",
        "accent_hover": "#a96721",
        "accent_text": "#3e2f26",
        "danger": "#8c2f24",
        "danger_hover": "#6f251c",
        "danger_text": "#8c2f24",
        "success": "#6f8f52",
        "success_hover": "#5b7743",
        "success_text": "#182a10",
        "info": "#f8edca",
        "info_hover": "#ecd9a8",
        "info_text": "#3e2f26",
        "border": "#8c2f24",
        "entry_bg": "#fff4d0",
        "selection_bg": "#c9822b",
        "selection_text": "#3e2f26",
    },

    "coastal_blue": {
        "background": "#164e63",
        "surface": "#e0f2fe",
        "surface_alt": "#bae6fd",
        "text": "#164e63",
        "muted": "#477184",
        "heading": "#075985",
        "accent": "#fbbf24",
        "accent_hover": "#f59e0b",
        "accent_text": "#164e63",
        "danger": "#075985",
        "danger_hover": "#b91c1c",
        "danger_text": "#fff7ed",
        "success": "#22c55e",
        "success_hover": "#16a34a",
        "success_text": "#052e16",
        "info": "#f0fdfa",
        "info_hover": "#ccfbf1",
        "info_text": "#164e63",
        "border": "#075985",
        "entry_bg": "#f0f9ff",
        "selection_bg": "#fbbf24",
        "selection_text": "#164e63",
    },
    "forest_cream": {
         "background": "#2f4f3e",
         "surface": "#f5efd7",
         "surface_alt": "#e8ddb5",
         "text": "#2f4f3e",
         "muted": "#647267",
         "heading": "#6b3f2a",
         "accent": "#d6a94a",
         "accent_hover": "#b98d35",
         "accent_text": "#2f4f3e",
         "danger": "#6b3f2a",
         "danger_hover": "#7c302a",
         "danger_text": "#2f4f3e",
         "success": "#7ea66a",
         "success_hover": "#668c54",
         "success_text": "#14301e",
         "info": "#dde8c8",
         "info_hover": "#c9d9b3",
         "info_text": "#2f4f3e",
         "border": "#6b3f2a",
         "entry_bg": "#fff8e3",
         "selection_bg": "#d6a94a",
         "selection_text": "#2f4f3e",
     },
    "terracotta": {
        "background": "#5c2e24",
        "surface": "#ffe8cc",
        "surface_alt": "#f9c89b",
        "text": "#5c2e24",
        "muted": "#866254",
        "heading": "#b4422c",
        "accent": "#e08e45",
        "accent_hover": "#c77532",
        "accent_text": "#5c2e24",
        "danger": "#9f2d20",
        "danger_hover": "#7f241a",
        "danger_text": "#b4422c",
        "success": "#8faf5d",
        "success_hover": "#728f48",
        "success_text": "#1f3211",
        "info": "#fff3e0",
        "info_hover": "#ffe0b8",
        "info_text": "#5c2e24",
        "border": "#b4422c",
        "entry_bg": "#fff4df",
        "selection_bg": "#e08e45",
        "selection_text": "#5c2e24",
    }
}




class InterraillerApp:
    def __init__(self, root, network):
        self.root = root
        self.network = network
        self.available_cities = network.get_available_cities()

        self.selected_cities = []
        self.profile_name = None
        self.weights = None
        self.result = None

        self.current_theme_name = CURRENT_THEME
        self.theme = THEMES[self.current_theme_name]

        self.build_gui()

    # theme build

    def c(self, colour_name):
        return self.theme[colour_name]

    def set_theme(self, theme_name):
        if theme_name not in THEMES:
            messagebox.showerror(f"Theme {theme_name} does not exist.")
            return

        self.theme = THEMES[theme_name]

    def make_button(
        self,
        parent,
        text,
        command,
        style="accent",
        width=24
    ):
        if style == "accent":
            bg = self.c("accent")
            fg = self.c("accent_text")
            active_bg = self.c("accent_hover")
            active_fg = self.c("accent_text")
        elif style == "danger":
            bg = self.c("danger")
            fg = self.c("danger_text")
            active_bg = self.c("danger_hover")
            active_fg = self.c("danger_text")
        elif style == "success":
            bg = self.c("success")
            fg = self.c("success_text")
            active_bg = self.c("success_hover")
            active_fg = self.c("success_text")
        elif style == "info":
            bg = self.c("info")
            fg = self.c("info_text")
            active_bg = self.c("info_hover")
            active_fg = self.c("info_text")
        else:
            bg = self.c("accent")
            fg = self.c("accent_text")
            active_bg = self.c("accent_hover")
            active_fg = self.c("accent_text")

        button = tk.Button(
            parent,
            text=text,
            command=command,
            font=("Helvetica", 11, "bold"),
            bg=bg,
            fg=fg,
            activebackground=active_bg,
            activeforeground=active_fg,
            relief="flat",
            bd=0,
            cursor="hand2",
            width=width,
            pady=8
        )

        return button

    def style_option_menu(self, menu):
        menu.config(
            font=("Helvetica", 11),
            bg=self.c("entry_bg"),
            fg=self.c("text"),
            activebackground=self.c("accent"),
            activeforeground=self.c("accent_text"),
            relief="flat",
            bd=0,
            highlightthickness=0
        )

        menu["menu"].config(
            bg=self.c("entry_bg"),
            fg=self.c("text"),
            activebackground=self.c("accent"),
            activeforeground=self.c("accent_text")
        )

    # GUI parts

    def build_gui(self):
        self.root.title("Interrailler - Route Optimiser")
        self.root.geometry("1200x850")
        self.root.configure(bg=self.c("background"))
        self.root.resizable(False, False)

        self.build_header()
        self.build_main_content()
        self.build_footer()

    def build_header(self):
        header = tk.Frame(self.root, bg=self.c("background"))
        header.pack(fill="x", padx=30, pady=(25, 10))

        title_block = tk.Frame(header, bg=self.c("background"))
        title_block.pack(side="left")

        tk.Label(
            title_block,
            text="Interrailler",
            font=("Helvetica", 32, "bold"),
            fg=self.c("surface"),
            bg=self.c("background")
        ).pack(anchor="w")

        tk.Label(
            title_block,
            text="Let's plan your next train journey !!",
            font=("Helvetica", 13),
            fg=self.c("surface_alt"),
            bg=self.c("background")
        ).pack(anchor="w", pady=(4, 0))

        right_header = tk.Frame(header, bg=self.c("background"))
        right_header.pack(side="right", anchor="ne")

        theme_button = self.make_button(
            right_header,
            f"Theme: {self.current_theme_name.replace('_', ' ').title()}",
            self.cycle_theme,
            style="info",
            width=20
        )
        theme_button.pack(anchor="e", pady=(0, 8))

        self.status_label = tk.Label(
            right_header,
            text="Choose a profile, select cities, then run the optimiser.",
            font=("Helvetica", 11, "bold"),
            fg=self.c("surface"),
            bg=self.c("background"),
            wraplength=330,
            justify="right"
        )
        self.status_label.pack(anchor="e")

    def cycle_theme(self):
        theme_names = list(THEMES.keys())

        current_index = theme_names.index(self.current_theme_name)
        next_index = (current_index + 1) % len(theme_names)

        self.current_theme_name = theme_names[next_index]
        self.theme = THEMES[self.current_theme_name]

        self.rebuild_gui_after_theme_change()

    def rebuild_gui_after_theme_change(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.build_gui()

        self.refresh_available_list()
        self.refresh_selected_list()
        self.refresh_endpoint_menus()
        self.update_summary_text()

        if self.profile_name is not None:
            self.profile_display.config(
                text=f"Selected: {self.profile_name}\nWeights: time={self.weights[0]}, scenic={self.weights[1]}, changes={self.weights[2]}",
                fg=self.c("heading")
            )

    def build_main_content(self):
        main = tk.Frame(self.root, bg=self.c("background"))
        main.pack(fill="both", expand=True, padx=30, pady=15)

        PANEL_HEIGHT = 640
        SIDE_PANEL_WIDTH = 310
        MIDDLE_PANEL_WIDTH = 390

        def make_panel(parent, width):
            panel = tk.Frame(
                parent,
                bg=self.c("surface"),
                width=width,
                height=PANEL_HEIGHT,
                highlightbackground=self.c("border"),
                highlightthickness=2
            )
            panel.grid_propagate(False)
            panel.pack_propagate(False)
            return panel

        self.left_panel = make_panel(main, SIDE_PANEL_WIDTH)
        self.left_panel.grid(row=0, column=0, padx=(0, 20), sticky="n")

        self.middle_panel = make_panel(main, MIDDLE_PANEL_WIDTH)
        self.middle_panel.grid(row=0, column=1, padx=20, sticky="n")

        self.right_panel = make_panel(main, SIDE_PANEL_WIDTH)
        self.right_panel.grid(row=0, column=2, padx=(20, 0), sticky="n")

        self.build_profile_panel()
        self.build_city_panel()
        self.build_summary_panel()

    def make_panel_title(self, parent, title, subtitle):
        tk.Label(
            parent,
            text=title,
            font=("Helvetica", 18, "bold"),
            fg=self.c("heading"),
            bg=self.c("surface")
        ).pack(anchor="w", padx=20, pady=(20, 4))

        tk.Label(
            parent,
            text=subtitle,
            font=("Helvetica", 10),
            fg=self.c("muted"),
            bg=self.c("surface"),
            wraplength=260,
            justify="left"
        ).pack(anchor="w", padx=20, pady=(0, 15))

    # profiles panel

    def build_profile_panel(self):
        self.make_panel_title(
            self.left_panel,
            "Route profile",
            "Choose how the optimiser should judge route quality."
        )

        profiles = [
            ("Fastest route", "Prioritises shorter travel time.", (2.5, 0.0, 1.0)),
            ("Scenic route", "Prioritises scenic scores more heavily.", (0.8, 2.5, 0.8)),
            ("Fewest changes", "Strongly penalises extra train changes.", (1.0, 0.0, 3.0)),
            ("Balanced route", "Balances time, scenery and changes.", (1.0, 1.0, 1.0)),
        ]

        for name, description, weights in profiles:
            frame = tk.Frame(self.left_panel, bg=self.c("surface_alt"))
            frame.pack(fill="x", padx=20, pady=7)

            tk.Label(
                frame,
                text=name,
                font=("Helvetica", 12, "bold"),
                fg=self.c("heading"),
                bg=self.c("surface_alt")
            ).pack(anchor="w", padx=12, pady=(8, 0))

            tk.Label(
                frame,
                text=description,
                font=("Helvetica", 9),
                fg=self.c("text"),
                bg=self.c("surface_alt"),
                wraplength=240,
                justify="left"
            ).pack(anchor="w", padx=12, pady=(2, 8))

            self.make_button(
                frame,
                "Select",
                lambda n=name, w=weights: self.select_profile(n, w),
                style="accent",
                width=10
            ).pack(anchor="e", padx=12, pady=(0, 10))

        self.make_button(
            self.left_panel,
            "Custom weights",
            self.open_custom_weights_popup,
            style="danger",
            width=22
        ).pack(pady=5)

        self.profile_display = tk.Label(
            self.left_panel,
            text="No profile selected",
            font=("Helvetica", 11, "bold"),
            fg=self.c("danger"),
            bg=self.c("surface"),
            wraplength=300,
            justify="center"
        )
        self.profile_display.pack(pady=10)

    def select_profile(self, name, weights):
        self.profile_name = name
        self.weights = weights

        self.profile_display.config(
            text=f"Selected: {name}\nWeights: time={weights[0]}, scenic={weights[1]}, changes={weights[2]}",
            fg=self.c("heading")
        )

        self.status_label.config(text=f"Profile selected: {name}")
        self.update_summary_text()

    def open_custom_weights_popup(self):
        popup = tk.Toplevel(self.root)
        popup.title("Custom weights")
        popup.geometry("400x340")
        popup.configure(bg=self.c("background"))
        popup.resizable(False, False)
        popup.transient(self.root)
        popup.grab_set()

        tk.Label(
            popup,
            text="Custom weights",
            font=("Helvetica", 22, "bold"),
            fg=self.c("surface"),
            bg=self.c("background")
        ).pack(pady=(25, 5))

        tk.Label(
            popup,
            text="Higher values mean the factor is more important",
            font=("Helvetica", 10),
            fg=self.c("surface_alt"),
            bg=self.c("background")
        ).pack(pady=(0, 18))

        time_entry = self.create_popup_entry(popup, "Reducing travel time")
        scenic_entry = self.create_popup_entry(popup, "Scenic value")
        changes_entry = self.create_popup_entry(popup, "Reducing changes")

        def save_custom():
            try:
                time_weight = float(time_entry.get())
                scenic_weight = float(scenic_entry.get())
                changes_weight = float(changes_entry.get())

                if time_weight < 0 or scenic_weight < 0 or changes_weight < 0:
                    messagebox.showerror("Invalid input", "Weights cannot be negative")
                    return

                self.select_profile(
                    "Custom weights",
                    (time_weight, scenic_weight, changes_weight)
                )
                popup.destroy()

            except ValueError:
                messagebox.showerror("Invalid input", "Please enter numbers only")

        self.make_button(
            popup,
            "Save weights",
            save_custom,
            style="accent",
            width=18
        ).pack(pady=18)

    def create_popup_entry(self, parent, label_text):
        frame = tk.Frame(parent, bg=self.c("background"))
        frame.pack(pady=6)

        tk.Label(
            frame,
            text=label_text,
            font=("Helvetica", 11, "bold"),
            fg=self.c("surface"),
            bg=self.c("background"),
            width=22,
            anchor="w"
        ).pack(side="left", padx=(0, 10))

        entry = tk.Entry(
            frame,
            font=("Helvetica", 11),
            bg=self.c("entry_bg"),
            fg=self.c("text"),
            insertbackground=self.c("text"),
            relief="flat",
            width=10
        )
        entry.pack(side="left", ipady=6)

        return entry

    # city panel

    def build_city_panel(self):
        self.make_panel_title(
            self.middle_panel,
            "City selection",
            "Choose cities from the available list and add them to your journey"
        )

        search_frame = tk.Frame(self.middle_panel, bg=self.c("surface"))
        search_frame.pack(fill="x", padx=20, pady=(0, 10))

        tk.Label(
            search_frame,
            text="Search city:",
            font=("Helvetica", 10, "bold"),
            fg=self.c("text"),
            bg=self.c("surface")
        ).pack(anchor="w")

        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", lambda *args: self.refresh_available_list())

        self.search_entry = tk.Entry(
            search_frame,
            textvariable=self.search_var,
            font=("Helvetica", 12),
            bg=self.c("entry_bg"),
            fg=self.c("text"),
            insertbackground=self.c("text"),
            relief="flat"
        )
        self.search_entry.pack(fill="x", ipady=8, pady=(5, 0))

        tk.Label(
            self.middle_panel,
            text="Available cities",
            font=("Helvetica", 11, "bold"),
            fg=self.c("heading"),
            bg=self.c("surface")
        ).pack(anchor="w", padx=20, pady=(5, 3))

        self.available_listbox = tk.Listbox(
            self.middle_panel,
            height=11,
            font=("Helvetica", 11),
            bg=self.c("entry_bg"),
            fg=self.c("text"),
            selectbackground=self.c("selection_bg"),
            selectforeground=self.c("selection_text"),
            relief="flat",
            activestyle="none"
        )
        self.available_listbox.pack(fill="x", padx=20)

        self.refresh_available_list()

        self.make_button(
            self.middle_panel,
            "Add selected city",
            self.add_selected_city,
            style="accent",
            width=28
        ).pack(pady=12)

        tk.Label(
            self.middle_panel,
            text="Selected cities",
            font=("Helvetica", 11, "bold"),
            fg=self.c("heading"),
            bg=self.c("surface")
        ).pack(anchor="w", padx=20, pady=(3, 3))

        self.selected_listbox = tk.Listbox(
            self.middle_panel,
            height=8,
            font=("Helvetica", 11),
            bg=self.c("entry_bg"),
            fg=self.c("text"),
            selectbackground=self.c("danger"),
            selectforeground=self.c("danger_text"),
            relief="flat",
            activestyle="none"
        )
        self.selected_listbox.pack(fill="x", padx=20)

        self.make_button(
            self.middle_panel,
            "Remove selected city",
            self.remove_selected_city,
            style="danger",
            width=28
        ).pack(pady=12)

    def refresh_available_list(self):
        search_text = self.search_var.get().lower().strip()

        self.available_listbox.delete(0, tk.END)

        for city in self.available_cities:
            if search_text in city.lower() and city not in self.selected_cities:
                self.available_listbox.insert(tk.END, city)

    def add_selected_city(self):
        selection = self.available_listbox.curselection()

        if not selection:
            messagebox.showerror("No city selected", "Please select a city to add")
            return

        city = self.available_listbox.get(selection[0])

        if city in self.selected_cities:
            messagebox.showerror("Duplicate city", "This city has already been added")
            return

        if len(self.selected_cities) >= 20:
            messagebox.showerror("Too many cities", "Please choose no more than 20 cities")
            return

        self.selected_cities.append(city)
        self.refresh_available_list()
        self.refresh_selected_list()
        self.refresh_endpoint_menus()
        self.update_summary_text()

    def remove_selected_city(self):
        selection = self.selected_listbox.curselection()

        if not selection:
            messagebox.showerror("No city selected", "Please select a city to remove.")
            return

        city = self.selected_listbox.get(selection[0])
        self.selected_cities.remove(city)

        self.refresh_available_list()
        self.refresh_selected_list()
        self.refresh_endpoint_menus()
        self.update_summary_text()

    def refresh_selected_list(self):
        self.selected_listbox.delete(0, tk.END)

        for city in self.selected_cities:
            self.selected_listbox.insert(tk.END, city)

    #summary

    def build_summary_panel(self):
        self.make_panel_title(
            self.right_panel,
            "Journey setup",
            "Choose optional start and end cities, then run the optimiser."
        )

        tk.Label(
            self.right_panel,
            text="Optional start city",
            font=("Helvetica", 11, "bold"),
            fg=self.c("heading"),
            bg=self.c("surface")
        ).pack(anchor="w", padx=20, pady=(5, 4))

        self.start_var = tk.StringVar(value="No fixed start")
        self.start_menu = tk.OptionMenu(self.right_panel, self.start_var, "No fixed start")
        self.style_option_menu(self.start_menu)
        self.start_menu.pack(fill="x", padx=20, pady=(0, 12))

        tk.Label(
            self.right_panel,
            text="Optional end city",
            font=("Helvetica", 11, "bold"),
            fg=self.c("heading"),
            bg=self.c("surface")
        ).pack(anchor="w", padx=20, pady=(5, 4))

        self.end_var = tk.StringVar(value="No fixed end")
        self.end_menu = tk.OptionMenu(self.right_panel, self.end_var, "No fixed end")
        self.style_option_menu(self.end_menu)
        self.end_menu.pack(fill="x", padx=20, pady=(0, 18))

        self.summary_text = tk.Text(
            self.right_panel,
            height=14,
            width=28,
            font=("Helvetica", 10),
            bg=self.c("entry_bg"),
            fg=self.c("text"),
            relief="flat",
            wrap="word"
        )
        self.summary_text.pack(padx=20, pady=10)
        self.summary_text.config(state="disabled")

        self.update_summary_text()

        self.make_button(
            self.right_panel,
            "Run optimiser",
            self.run_optimiser,
            style="success",
            width=22
        ).pack(pady=(12, 6))

        self.make_button(
            self.right_panel,
            "Display graphs",
            self.display_graphs,
            style="info",
            width=28
        ).pack(pady=5)

        self.make_button(
            self.right_panel,
            "Reset setup",
            self.reset_setup,
            style="danger",
            width=28
        ).pack(pady=5)

    def refresh_endpoint_menus(self):
        start_options = ["No fixed start"] + self.selected_cities
        end_options = ["No fixed end"] + self.selected_cities

        self.start_menu["menu"].delete(0, "end")
        for option in start_options:
            self.start_menu["menu"].add_command(
                label=option,
                command=tk._setit(self.start_var, option, self.update_summary_text)
            )

        self.end_menu["menu"].delete(0, "end")
        for option in end_options:
            self.end_menu["menu"].add_command(
                label=option,
                command=tk._setit(self.end_var, option, self.update_summary_text)
            )

        if self.start_var.get() not in start_options:
            self.start_var.set("No fixed start")

        if self.end_var.get() not in end_options:
            self.end_var.set("No fixed end")

    def update_summary_text(self, *args):
        self.summary_text.config(state="normal")
        self.summary_text.delete("1.0", tk.END)

        profile = self.profile_name if self.profile_name else "Not selected"
        weights = self.weights if self.weights else "N/A"

        start = self.start_var.get()
        end = self.end_var.get()

        summary = (
            f"Profile:\n{profile}\n\n"
            f"Weights:\n{weights}\n\n"
            f"Selected cities ({len(self.selected_cities)}):\n"
            f"{', '.join(self.selected_cities) if self.selected_cities else 'None yet'}\n\n"
            f"Start city:\n{start}\n\n"
            f"End city:\n{end}\n\n"
            f"Ready status:\n"
        )

        if self.profile_name and len(self.selected_cities) >= 2:
            summary += "Ready to run."
        else:
            summary += "Choose a profile and at least 2 cities."

        self.summary_text.insert("1.0", summary)
        self.summary_text.config(state="disabled")

    def reset_setup(self):
        self.selected_cities = []
        self.start_var.set("No fixed start")
        self.end_var.set("No fixed end")
        self.profile_name = None
        self.weights = None
        self.result = None

        self.profile_display.config(text="No profile selected", fg=self.c("danger"))
        self.status_label.config(text="Choose a profile, select cities, then run the optimiser")

        self.refresh_available_list()
        self.refresh_selected_list()
        self.refresh_endpoint_menus()
        self.update_summary_text()

    #  footer

    def build_footer(self):
        footer = tk.Frame(self.root, bg=self.c("background"))
        footer.pack(fill="x", padx=30, pady=(0, 20))

        tk.Label(
            footer,
            text="Click Display graphs after running the optimiser to view analysis graphs",
            font=("Helvetica", 10),
            fg=self.c("surface_alt"),
            bg=self.c("background")
        ).pack(side="left")

        tk.Label(
            footer,
            text="V: 2.0",
            font=("Helvetica", 10, "bold"),
            fg=self.c("surface"),
            bg=self.c("background")
        ).pack(side="right")


    def display_graphs(self):
        if self.result is None:
            messagebox.showerror(
                "No results yet",
                "Please run the optimiser before displaying graphs"
            )
            return

        best_stats = self.result["best_stats"]
        ga = self.result["ga"]

        plot_route_summary(best_stats)
        plot_ga_analysis(ga)

        plt.show()

    def run_optimiser(self):
        if self.weights is None:
            messagebox.showerror("Missing profile", "Please choose a route profile.")
            return

        if len(self.selected_cities) < 2:
            messagebox.showerror("Missing cities", "Please choose at least 2 cities.")
            return

        start_city = None
        end_city = None

        if self.start_var.get() != "No fixed start":
            start_city = self.start_var.get()

        if self.end_var.get() != "No fixed end":
            end_city = self.end_var.get()

        if start_city is not None and end_city is not None and start_city == end_city:
            messagebox.showerror("Invalid endpoints", "Start city and end city cannot be the same.")
            return

        self.status_label.config(text="Running optimiser...")
        self.root.update_idletasks()

        time_weight, scenic_weight, changes_weight = self.weights

        ga = GeneticAlgorithm(
            rail_network=self.network,
            cities=self.selected_cities,
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
            messagebox.showerror("No valid route", "No valid route could be found using the dataset")
            self.status_label.config(text="No valid route found.")
            return

        greedy_route = greedy_baseline(
            self.network,
            self.selected_cities,
            start_city,
            end_city,
            time_weight,
            scenic_weight,
            changes_weight
        )

        greedy_stats = ga.calculate_route_stats(greedy_route)
        greedy_score = ga.fitness(greedy_route)

        self.result = {
            "ga": ga,
            "best_route": best_route,
            "best_stats": best_stats,
            "best_score": best_score,
            "greedy_route": greedy_route,
            "greedy_stats": greedy_stats,
            "greedy_score": greedy_score,
            "profile_name": self.profile_name
        }

        self.status_label.config(text="Optimisation complete.")
        self.show_result_popup()
        print_console_results(self.network, self.result)

        messagebox.showinfo(
            "Optimisation complete",
            "The route has been optimised. Click 'Display graphs' to view the analysis graphs"
        )

    def show_result_popup(self):
        result = self.result

        popup = tk.Toplevel(self.root)
        popup.title("Optimised journey result")
        popup.geometry("720x520")
        popup.configure(bg=self.c("background"))
        popup.transient(self.root)

        tk.Label(
            popup,
            text="Optimised journey",
            font=("Helvetica", 24, "bold"),
            fg=self.c("surface"),
            bg=self.c("background")
        ).pack(pady=(22, 5))

        tk.Label(
            popup,
            text=f"Profile used: {result['profile_name']}",
            font=("Helvetica", 11),
            fg=self.c("surface_alt"),
            bg=self.c("background")
        ).pack(pady=(0, 15))

        output = tk.Text(
            popup,
            font=("Helvetica", 11),
            bg=self.c("surface"),
            fg=self.c("text"),
            relief="flat",
            wrap="word",
            height=20,
            width=78
        )
        output.pack(padx=25, pady=10)

        best_stats = result["best_stats"]

        content = (
            "Selected City Visit Order:\n"
            + " -> ".join(result["best_route"])
            + "\n\nFull Rail Path Including Interchange Cities:\n"
            + " -> ".join(best_stats["full_path"])
            + "\n\nJourney Statistics:\n"
            + f"Total travel time: {round(best_stats['time'], 2)} hours\n"
            + f"Total scenic score: {round(best_stats['scenic'], 2)}\n"
            + f"Total changes: {best_stats['changes']}\n"
            + f"GA fitness score: {round(result['best_score'], 2)}\n"
        )

        if result["greedy_stats"] is not None:
            content += (
                f"\nGreedy baseline fitness score: {round(result['greedy_score'], 2)}\n"
            )

            if result["best_score"] > result["greedy_score"]:
                content += "\nThe genetic algorithm found a better route than the greedy baseline."
            elif result["best_score"] == result["greedy_score"]:
                content += "\nThe genetic algorithm matched the greedy baseline."
            else:
                content += "\nThe greedy baseline performed better for this particular run."

        output.insert("1.0", content)
        output.config(state="disabled")

        self.make_button(
            popup,
            "Close",
            popup.destroy,
            style="accent",
            width=16
        ).pack(pady=10)



# output,graph functions


def print_console_results(network, result):
    best_route = result["best_route"]
    best_stats = result["best_stats"]
    best_score = result["best_score"]
    greedy_route = result["greedy_route"]
    greedy_stats = result["greedy_stats"]
    greedy_score = result["greedy_score"]

    print("\n" + "=" * 70)
    print("OPTIMISED JOURNEY RESULT")
    print("=" * 70)

    print("\nSelected City Visit Order:")
    print(" -> ".join(best_route))

    print("\nFull Rail Path Including Interchange Cities:")
    print(" -> ".join(best_stats["full_path"]))

    print("\nJourney Statistics:")
    print(f"Total travel time: {round(best_stats['time'], 2)} hours")
    print(f"Total scenic score: {round(best_stats['scenic'], 2)}")
    print(f"Total changes: {best_stats['changes']}")
    print(f"Fitness score: {round(best_score, 2)}")

    print("\nDetailed Rail Legs:")

    full_path = best_stats["full_path"]

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
                f"Try checking whether an overnight train is available or breaking the journey."
            )

    if not found_long_leg:
        print("No individual rail leg is over 7 hours.")

    print("\nGreedy Baseline Selected City Visit Order:")
    print(" -> ".join(greedy_route))

    if greedy_stats is not None:
        print("\nGreedy Baseline Full Rail Path Including Interchange Cities:")
        print(" -> ".join(greedy_stats["full_path"]))

        print("\nComparison:")
        print(f"GA fitness score: {round(best_score, 2)}")
        print(f"Greedy baseline fitness score: {round(greedy_score, 2)}")
    else:
        print("The greedy baseline could not produce a valid route.")


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


# main program


def main():
    network = RailNetwork()

    try:
        network.load_from_csv("routes.csv")
    except FileNotFoundError:
        print("Error: routes.csv was not found")
        print("Make sure routes.csv is in the same folder as your Python file")
        return
    except ValueError as error:
        print("CSV error:", error)
        return

    root = tk.Tk()
    app = InterraillerApp(root, network)
    root.mainloop()


if __name__ == "__main__":
    main()