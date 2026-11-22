#importds, rail network, dijkstra

import csv
import heapq
import math
import random
import tkinter as tk
from pathlib import Path
from tkinter import messagebox

import matplotlib.pyplot as plt




class RailNetwork:
    def __init__(self, filename):
        self.routes = {}
        self.neighbours = {}

        with open(filename, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            required = {"from_city", "to_city", "time_hours", "scenic_score", "changes"}

            if not reader.fieldnames or not required.issubset(reader.fieldnames):
                raise ValueError("CSV columns missing")

            for row in reader:
                a = row["from_city"].strip()
                b = row["to_city"].strip()
                hours = float(row["time_hours"])
                scenic = float(row["scenic_score"])
                changes = int(row["changes"])

                if not a or not b or a == b or hours <= 0:
                    raise ValueError("invalid rail connection")
                if not 0 <= scenic <= 10 or changes < 0:
                    raise ValueError("invalid scenic score or changes")

                # store both directions automatically
                #  dict avoids duplicate connections
                for start, end in [(a, b), (b, a)]:
                    key = (start, end)
                    values = (hours, scenic, changes)

                    if key in self.routes and self.routes[key] != values:
                        raise ValueError(f"conflicting route: {start} to {end}")

                    self.routes[key] = values
                    self.neighbours.setdefault(start, set()).add(end)

        if not self.routes:
            raise ValueError("no routes found")

    def cities(self):
        return sorted(self.neighbours)

    @staticmethod
    def edge_cost(hours, scenic, changes, weights, is_first_edge):
        # all algorithms use this same cost formula
        time_weight, scenic_weight, changes_weight = weights

        extra_transfer = 0 if is_first_edge else 1

        cost = (time_weight * hours + scenic_weight * (10 - scenic) + 2 * changes_weight * (changes + extra_transfer))
        return cost

    def shortest_path(self, start, finish, weights):
        # dijkstra's algorithm to find the lowest-cost connection.
        queue = [(0.0, start)]
        distances = {start: 0.0}
        previous = {start: None}

        while queue:
            cost, city = heapq.heappop(queue)

            if cost > distances[city]:
                continue
            if city == finish:
                break
            for neighbour in sorted(self.neighbours.get(city, [])):
                hours, scenic, changes = self.routes[(city, neighbour)]
                step_cost = self.edge_cost(hours, scenic, changes, weights, city == start)
                new_cost = cost + step_cost

                if new_cost < distances.get(neighbour, float("inf")):
                    distances[neighbour] = new_cost
                    previous[neighbour] = city
                    heapq.heappush(queue, (new_cost, neighbour))

        if finish not in distances:
            return None

        # reconstruct the shortest path.
        path = []
        city = finish

        while city is not None:
            path.append(city)
            city = previous[city]

        path.reverse()
        return path, distances[finish]

    def path_stats(self, path):
        total_time = 0
        total_scenic = 0
        total_changes = max(0, len(path) - 2)

        for a, b in zip(path, path[1:]):
            hours, scenic, changes = self.routes[(a, b)]
            total_time += hours
            total_scenic += scenic
            total_changes += changes

        return {
            "time": total_time,
            "scenic": total_scenic,
            "changes": total_changes
        }
#GA + greedy to compare

#  GENETIC ALGORITHM

class RouteOptimizer:
    def __init__(self, network, cities, start, finish, weights):
        self.network = network
        self.cities = cities[:]
        self.start = start
        self.finish = finish
        self.weights = weights

        self.best_scores = []
        self.mean_scores = []

        self.legs = {}

        for a in cities:
            for b in cities:
                if a != b:
                    result = network.shortest_path(a, b, weights)

                    if result is None:
                        raise ValueError(f"No route from {a} to {b}")

                    path, cost = result
                    stats = network.path_stats(path)
                    self.legs[(a, b)] = (path, cost, stats)

        # fixed endpoints cannot be moved.
        self.middle_cities = [city for city in cities if city != start and city != finish]

    def full_order(self, middle):
        order = []

        if self.start is not None:
            order.append(self.start)

        order.extend(middle)

        if self.finish is not None:
            order.append(self.finish)

        return order

    def fitness(self, order):
        # lower cost = higher fitness.
        total_cost = 0

        for a, b in zip(order, order[1:]):
            total_cost += self.legs[(a, b)][1]

        return -total_cost

    def route_details(self, order):
        details = {
            "time": 0,
            "scenic": 0,
            "changes": 0,
            "full_path": []
        }

        for a, b in zip(order, order[1:]):
            path, cost, stats = self.legs[(a, b)]

            details["time"] += stats["time"]
            details["scenic"] += stats["scenic"]
            details["changes"] += stats["changes"]

            if not details["full_path"]:
                details["full_path"].extend(path)
            else:
                details["full_path"].extend(path[1:])

        return details

    def tournament(self, population):
        # select the best of three random individuals
        contenders = random.sample(population, min(3, len(population)))

        return max(contenders,key=lambda individual: self.fitness(self.full_order(individual)))

    @staticmethod
    def crossover(parent1, parent2):
        # Keep a section from one parent
        # Fill remaining positions using the other parent
        if len(parent1) < 2:
            return parent1[:]

        left, right = sorted(random.sample(range(len(parent1)), 2))

        kept = parent1[left:right + 1]
        remaining = [city for city in parent2 if city not in kept]

        child = remaining[:left] + kept + remaining[left:]
        return child

    @staticmethod
    def mutate(individual, rate=0.15):
        child = individual[:]

        if len(child) > 1 and random.random() < rate:
            i, j = random.sample(range(len(child)), 2)
            child[i], child[j] = child[j], child[i]

        return child

    def run(self, population_size=80, generations=150):
        # create the initial population.
        population = [random.sample(self.middle_cities, len(self.middle_cities)) for _ in range(population_size)]

        for generation in range(generations):
            population.sort(key=lambda p: self.fitness(self.full_order(p)),reverse=True)

            scores = [self.fitness(self.full_order(p)) for p in population]

            self.best_scores.append(scores[0])
            self.mean_scores.append(sum(scores) / len(scores))

            # Elitism: preserve the two best routes
            next_population = [p[:] for p in population[:2]]

            while len(next_population) < population_size:
                parent1 = self.tournament(population)
                parent2 = self.tournament(population)

                child = self.crossover(parent1, parent2)
                child = self.mutate(child)

                next_population.append(child)

            population = next_population

        best = max(population,key=lambda p: self.fitness(self.full_order(p)))

        return self.full_order(best)

    def greedy(self):
        # greedy baseline: repeatedly choose the cheapest next city
        # if no start is fixed try every possible start
        if self.start is not None:
            starts = [self.start]
        else:
            starts = [c for c in self.cities if c != self.finish]

        best_order = None

        for starting_city in starts:
            order = [starting_city]

            remaining = [c for c in self.cities if c != starting_city and c != self.finish]

            while remaining:
                current = order[-1]

                next_city = min(remaining,key=lambda c: self.legs[(current, c)][1])

                order.append(next_city)
                remaining.remove(next_city)

            if self.finish is not None:
                order.append(self.finish)

            if best_order is None or self.fitness(order) > self.fitness(best_order):
                best_order = order

        return best_order


# PART 3: GUI THEMES AND PROFILES

THEMES = {
    "navy_modern": dict(
        background="#0f172a", surface="#1e293b",
        surface_alt="#334155", text="#f8fafc",
        muted="#cbd5e1", heading="#f8fafc",
        accent="#38bdf8", accent_text="#082f49",
        danger="#fb7185", success="#22c55e",
        info="#bae6fd", border="#38bdf8",
        entry_bg="#334155", selection_bg="#38bdf8"
    ),

    "vintage_rail": dict(
        background="#3e2f26", surface="#f3e1b6",
        surface_alt="#e5c98f", text="#3e2f26",
        muted="#725f4a", heading="#8c2f24",
        accent="#c9822b", accent_text="#3e2f26",
        danger="#8c2f24", success="#6f8f52",
        info="#f8edca", border="#8c2f24",
        entry_bg="#fff4d0", selection_bg="#c9822b"
    ),

    "coastal_blue": dict(
        background="#164e63", surface="#e0f2fe",
        surface_alt="#bae6fd", text="#164e63",
        muted="#477184", heading="#075985",
        accent="#fbbf24", accent_text="#164e63",
        danger="#075985", success="#22c55e",
        info="#f0fdfa", border="#075985",
        entry_bg="#f0f9ff", selection_bg="#fbbf24"
    ),

    "forest_cream": dict(
        background="#2f4f3e", surface="#f5efd7",
        surface_alt="#e8ddb5", text="#2f4f3e",
        muted="#647267", heading="#6b3f2a",
        accent="#d6a94a", accent_text="#2f4f3e",
        danger="#6b3f2a", success="#7ea66a",
        info="#dde8c8", border="#6b3f2a",
        entry_bg="#fff8e3", selection_bg="#d6a94a"
    ),

    "terracotta": dict(
        background="#5c2e24", surface="#ffe8cc",
        surface_alt="#f9c89b", text="#5c2e24",
        muted="#866254", heading="#b4422c",
        accent="#e08e45", accent_text="#5c2e24",
        danger="#9f2d20", success="#8faf5d",
        info="#fff3e0", border="#b4422c",
        entry_bg="#fff4df", selection_bg="#e08e45"
    )
}


PROFILES = {
    "Fastest route": (2.5, 0.0, 1.0),
    "Scenic route": (0.8, 2.5, 0.8),
    "Fewest changes": (1.0, 0.0, 3.0),
    "Balanced route": (1.0, 1.0, 1.0)
}


# PART 4: MAIN GUI

class InterraillerApp:
    def __init__(self, root, network):
        self.root = root
        self.network = network

        self.available_cities = network.cities()
        self.selected_cities = []

        self.profile_name = None
        self.weights = None
        self.result = None

        self.theme_name = "navy_modern"

        self.search_var = tk.StringVar()
        self.start_var = tk.StringVar(value="No fixed start")
        self.end_var = tk.StringVar(value="No fixed end")

        self.search_var.trace_add("write", lambda *_: self.refresh_available())

        self.build_gui()

    # reusable GUI functions

    def label(self, parent, text, size=11, bold=False, colour="text", background="surface", wrap=260, **pack):
        font_style = "bold" if bold else "normal"

        widget = tk.Label(
            parent,
            text=text,
            font=("Helvetica", size, font_style),
            bg=self.theme[background],
            fg=self.theme[colour],
            wraplength=wrap,
            justify="left"
        )

        widget.pack(**pack)
        return widget

    def button(self, parent, text, command, kind="accent", width=22, **pack):
        bg = self.theme[kind]

        if kind in ("accent", "info", "success"):
            fg = self.theme["accent_text"]
        else:
            fg = "white"

        widget = tk.Button(
            parent,
            text=text,
            command=command,
            font=("Helvetica", 10, "bold"),
            width=width,
            pady=6,
            bg=bg,
            fg=fg,
            relief="flat",
            cursor="hand2"
        )

        widget.pack(**pack)
        return widget

    def panel(self, parent, width):
        frame = tk.Frame(
            parent,
            bg=self.theme["surface"],
            width=width,
            height=640,
            highlightbackground=self.theme["border"],
            highlightthickness=2
        )

        frame.pack_propagate(False)
        return frame

    def heading(self, parent, title, subtitle):
        self.label(
            parent, title, 18, True, "heading",
            pady=(16, 2), padx=18, anchor="w"
        )
        self.label(
            parent, subtitle, 10, colour="muted",
            padx=18, pady=(0, 12), anchor="w"
        )

    def build_gui(self):
        self.theme = THEMES[self.theme_name]

        # remove existing widgets when changing themes
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.title("Interrailler - Route Optimiser")
        self.root.geometry("1200x850")
        self.root.resizable(False, False)
        self.root.configure(bg=self.theme["background"])

        # header
        header = tk.Frame(self.root, bg=self.theme["background"])
        header.pack(fill="x", padx=30, pady=(25, 10))

        left_header = tk.Frame(header, bg=self.theme["background"])
        left_header.pack(side="left")

        self.label(
            left_header, "Interrailler", 32, True,
            "heading", "background", anchor="w"
        )
        self.label(
            left_header, "Let's plan your next train journey !!",
            13, colour="heading", background="background",
            wrap=500, anchor="w"
        )

        right_header = tk.Frame(header, bg=self.theme["background"])
        right_header.pack(side="right", anchor="ne")

        self.button(
            right_header,
            "Theme: " + self.theme_name.replace("_", " ").title(),
            self.cycle_theme,
            "info", 24, anchor="e", pady=(0, 10)
        )

        self.status = self.label(
            right_header,
            "Choose a profile and at least two cities.",
            10, True, "heading", "background", anchor="e"
        )

        # Main panels
        main = tk.Frame(self.root, bg=self.theme["background"])
        main.pack(
            fill="both", expand=True,
            padx=30, pady=(10, 5)
        )

        left = self.panel(main, 310)
        middle = self.panel(main, 390)
        right = self.panel(main, 310)

        left.grid(row=0, column=0, padx=(0, 25), sticky="n")
        middle.grid(row=0, column=1, padx=(0, 25), sticky="n")
        right.grid(row=0, column=2, sticky="n")

        self.build_profile_panel(left)
        self.build_city_panel(middle)
        self.build_summary_panel(right)

        # Footer
        footer = tk.Frame(self.root, bg=self.theme["background"])
        footer.pack(fill="x", padx=30, pady=(0, 20))

        self.label(
            footer,
            "click display graphs after optimising to view analysis graphs.",
            10, colour="heading", background="background",
            wrap=500, side="left"
        )

        self.label(
            footer, "V: 2.1", 10, True,
            "heading", "background", side="right"
        )

        self.refresh_available()
        self.refresh_selected()
        self.refresh_endpoints()
        self.update_summary()

        if self.profile_name is not None:
            self.profile_label.configure(text=f"Selected: {self.profile_name}\nWeights: {self.weights}")
            self.status.configure(text="Profile selected: " + self.profile_name)

    def build_profile_panel(self, panel):
        self.heading(panel, "route profile", "choose how the optimiser should judge route quality.")

        descriptions = [
            "Prioritises shorter travel time.",
            "Prioritises more scenic connections.",
            "Strongly penalises extra train changes.",
            "Balances time, scenery and changes."
        ]

        for (name, weights), description in zip(PROFILES.items(), descriptions):
            frame = tk.Frame(panel, bg=self.theme["surface_alt"])
            frame.pack(fill="x", padx=18, pady=5)

            self.label(
                frame, name, 11, True,
                "heading", "surface_alt",
                padx=10, pady=(6, 0), anchor="w"
            )

            self.label(
                frame, description, 9,
                colour="text", background="surface_alt",
                padx=10, anchor="w"
            )

            self.button(
                frame, "Select",
                lambda n=name, w=weights: self.select_profile(n, w),
                width=10, anchor="e",
                padx=10, pady=(0, 6)
            )

        self.button(
            panel, "Custom weights", self.custom_weights,
            "danger", 20, pady=(8, 4)
        )

        self.profile_label = self.label(
            panel, "No profile selected",
            10, True, "heading", pady=6
        )


# PART 5: GUI PANELS AND SETTINGS

    def build_city_panel(self, panel):
        self.heading(panel, "city selection","choose cities from the available list and add them to your journey.")

        self.label(panel, "search city:", 10, True, "heading", padx=18, anchor="w")

        entry = tk.Entry(
            panel,
            textvariable=self.search_var,
            font=("Helvetica", 11),
            bg=self.theme["entry_bg"],
            fg=self.theme["text"],
            relief="flat"
        )
        entry.pack(fill="x", padx=18, ipady=6, pady=(5, 10))

        self.label(panel, "Available cities", 10, True, "heading", padx=18, anchor="w")

        self.available_listbox = tk.Listbox(
            panel,
            height=10,
            font=("Helvetica", 11),
            bg=self.theme["entry_bg"],
            fg=self.theme["text"],
            selectbackground=self.theme["selection_bg"],
            selectforeground=self.theme["accent_text"],
            relief="flat"
        )
        self.available_listbox.pack(fill="x", padx=18, pady=(3, 6))

        self.button(panel, "Add selected city", self.add_city, width=24, pady=4)

        self.label(panel, "Selected cities", 10, True, "heading", padx=18, pady=(8, 0), anchor="w")

        self.selected_listbox = tk.Listbox(
            panel,
            height=7,
            font=("Helvetica", 11),
            bg=self.theme["entry_bg"],
            fg=self.theme["text"],
            selectbackground=self.theme["selection_bg"],
            selectforeground=self.theme["accent_text"],
            relief="flat"
        )
        self.selected_listbox.pack(fill="x", padx=18, pady=(3, 6))

        self.button(panel, "Remove selected city", self.remove_city, "danger", 24, pady=4)

    def build_summary_panel(self, panel):
        self.heading(panel, "Journey setup", "Choose optional endpoints and run the optimiser.")

        self.label(panel, "Optional start city", 10, True, "heading", padx=18, anchor="w")

        self.start_menu = tk.OptionMenu(panel, self.start_var, "No fixed start", command=lambda _: self.update_summary())
        self.style_menu(self.start_menu)

        self.label(panel, "Optional end city", 10, True, "heading", padx=18, pady=(8, 0), anchor="w")

        self.end_menu = tk.OptionMenu(panel, self.end_var, "No fixed end", command=lambda _: self.update_summary())
        self.style_menu(self.end_menu)

        self.summary = tk.Text(
            panel,
            height=15,
            width=28,
            font=("Helvetica", 10),
            bg=self.theme["entry_bg"],
            fg=self.theme["text"],
            relief="flat",
            wrap="word",
            state="disabled"
        )
        self.summary.pack(fill="x", padx=18, pady=(10, 8))

        self.button(panel, "Run optimiser", self.run_optimiser, "success", 22, pady=(4, 6))
        self.button(panel, "Display graphs", self.display_graphs, "info", 22, pady=4)
        self.button(panel, "Reset setup", self.reset, "danger", 22, pady=4)

    def style_menu(self, menu):
        menu.configure(
            bg=self.theme["entry_bg"],
            fg=self.theme["text"],
            activebackground=self.theme["selection_bg"],
            relief="flat",
            font=("Helvetica", 10)
        )
        menu.pack(fill="x", padx=18, pady=(4, 6))

        menu["menu"].configure(
            bg=self.theme["entry_bg"],
            fg=self.theme["text"]
        )

    def cycle_theme(self):
        names = list(THEMES)
        current_index = names.index(self.theme_name)
        next_index = (current_index + 1) % len(names)

        self.theme_name = names[next_index]
        self.build_gui()

    def select_profile(self, name, weights):
        self.profile_name = name
        self.weights = weights

        self.profile_label.configure(text=f"Selected: {name}\nWeights: {weights}")
        self.status.configure(text="Profile selected: " + name)
        self.update_summary()

    def custom_weights(self):
        popup = tk.Toplevel(self.root)
        popup.title("Custom weights")
        popup.geometry("410x350")
        popup.configure(bg=self.theme["background"])
        popup.resizable(False, False)
        popup.transient(self.root)
        popup.grab_set()

        self.label(popup, "Custom weights", 22, True,"heading", "background", pady=(20, 6))

        self.label(
            popup, "Higher values mean the factor is more important",
            10, colour="heading", background="background",
            pady=(0, 10)
        )

        entries = []

        for title in ("Reducing travel time", "Scenic value", "Reducing changes"):
            row = tk.Frame(popup, bg=self.theme["background"])
            row.pack(fill="x", padx=25, pady=7)

            self.label(row, title, 11, True, "heading", "background", side="left")

            entry = tk.Entry(
                row,
                width=10,
                font=("Helvetica", 11),
                bg=self.theme["entry_bg"],
                fg=self.theme["text"]
            )
            entry.pack(side="right")
            entries.append(entry)

        if self.weights:
            for entry, value in zip(entries, self.weights):
                entry.insert(0, str(value))

        def save():
            try:
                weights = tuple(float(entry.get()) for entry in entries)

                if any(not math.isfinite(value) or value < 0 for value in weights):
                    raise ValueError("Weights must be finite, non-negative numbers")

                if all(value == 0 for value in weights):
                    raise ValueError("At least one weight must be greater than zero")

            except ValueError as error:
                if "could not convert" in str(error):
                    messagebox.showerror("Invalid weights", "Please enter a number in each box")
                else:
                    messagebox.showerror("Invalid weights", str(error))
                return

            self.select_profile("Custom weights", weights)
            popup.destroy()

        self.button(popup, "Save weights", save, width=18, pady=(20, 0))


# PART 6: GUI INTERACTIONS AND OUTPUT

    def refresh_available(self):
        if (not hasattr(self, "available_listbox") or not self.available_listbox.winfo_exists()):
            return

        search = self.search_var.get().strip().lower()
        self.available_listbox.delete(0, tk.END)

        for city in self.available_cities:
            if (city not in self.selected_cities and search in city.lower()):
                self.available_listbox.insert(tk.END, city)

    def refresh_selected(self):
        self.selected_listbox.delete(0, tk.END)

        for city in self.selected_cities:
            self.selected_listbox.insert(tk.END, city)

    def refresh_endpoints(self):
        for menu, variable, default in ((self.start_menu, self.start_var, "No fixed start"), (self.end_menu, self.end_var, "No fixed end")):
            choices = [default] + self.selected_cities
            menu["menu"].delete(0, "end")

            for choice in choices:
                menu["menu"].add_command(label=choice, command=lambda c=choice, v=variable: (v.set(c), self.update_summary()))

            if variable.get() not in choices:
                variable.set(default)

    def add_city(self):
        selected = self.available_listbox.curselection()

        if not selected:
            messagebox.showerror("No city selected", "Select a city from the available list")
            return

        if len(self.selected_cities) >= 20:
            messagebox.showerror("Too many cities", "Choose no more than 20 cities")
            return

        city = self.available_listbox.get(selected[0])

        if city in self.selected_cities:
            messagebox.showerror("Duplicate city", "That city has already been added")
            return

        self.selected_cities.append(city)

        self.refresh_available()
        self.refresh_selected()
        self.refresh_endpoints()
        self.update_summary()

    def remove_city(self):
        selected = self.selected_listbox.curselection()

        if not selected:
            messagebox.showerror("No city selected", "Select a city to remove")
            return

        city = self.selected_listbox.get(selected[0])
        self.selected_cities.remove(city)

        self.refresh_available()
        self.refresh_selected()
        self.refresh_endpoints()
        self.update_summary()

    def update_summary(self):
        if (not hasattr(self, "summary") or not self.summary.winfo_exists()):
            return

        profile = self.profile_name or "Not selected"
        city_names = ", ".join(self.selected_cities) or "None yet"

        ready = (self.profile_name is not None and len(self.selected_cities) >= 2)

        info = (
            f"Profile:\n{profile}\n\n"
            f"Weights:\n{self.weights or 'N/A'}\n\n"
            f"Selected cities ({len(self.selected_cities)}):\n"
            f"{city_names}\n\n"
            f"Start city:\n{self.start_var.get()}\n\n"
            f"End city:\n{self.end_var.get()}\n\n"
            f"Ready status:\n"
        )

        if ready:
            info += "Ready to run."
        else:
            info += "Choose a profile and at least two cities."

        self.summary.configure(state="normal")
        self.summary.delete("1.0", tk.END)
        self.summary.insert("1.0", info)
        self.summary.configure(state="disabled")

    def reset(self):
        self.selected_cities.clear()
        self.profile_name = None
        self.weights = None
        self.result = None

        self.start_var.set("No fixed start")
        self.end_var.set("No fixed end")
        self.search_var.set("")

        self.profile_label.configure(text="No profile selected")
        self.status.configure(text="Choose a profile and at least two cities.")

        self.refresh_available()
        self.refresh_selected()
        self.refresh_endpoints()
        self.update_summary()

    def run_optimiser(self):
        if self.weights is None:
            messagebox.showerror("Missing profile", "Please choose a route profile")
            return

        if len(self.selected_cities) < 2:
            messagebox.showerror("Missing cities", "Please choose at least two cities")
            return

        start = self.start_var.get()
        finish = self.end_var.get()

        if start == "No fixed start":
            start = None

        if finish == "No fixed end":
            finish = None

        if start is not None and start == finish:
            messagebox.showerror("Invalid endpoints", "Start and end cities cannot be the same")
            return

        self.status.configure(text="Running optimiser...")
        self.root.update_idletasks()

        try:
            optimizer = RouteOptimizer(self.network, self.selected_cities, start, finish, self.weights)

            order = optimizer.run()
            greedy_order = optimizer.greedy()

            self.result = {
                "optimizer": optimizer,
                "order": order,
                "stats": optimizer.route_details(order),
                "fitness": optimizer.fitness(order),
                "greedy_order": greedy_order,
                "greedy_stats": optimizer.route_details(greedy_order),
                "greedy_fitness": optimizer.fitness(greedy_order)
            }

        except ValueError as error:
            self.status.configure(text="Unable to generate route")
            messagebox.showerror("No valid route", str(error))
            return

        self.status.configure(text="Optimisation complete")
        self.show_results()

    def show_results(self):
        result = self.result

        popup = tk.Toplevel(self.root)
        popup.title("Optimised journey result")
        popup.geometry("740x550")
        popup.configure(bg=self.theme["background"])
        popup.transient(self.root)

        self.label(popup, "Optimised journey", 24, True,"heading", "background", pady=(18, 4))

        self.label(popup, f"Profile used: {self.profile_name}", 11, colour="heading", background="background", pady=(0, 8))

        stats = result["stats"]
        ga_score = result["fitness"]
        greedy_score = result["greedy_fitness"]

        if ga_score > greedy_score:
            verdict = "Genetic algorithm scored higher"
        elif ga_score == greedy_score:
            verdict = "Both methods scored equally"
        else:
            verdict = "Greedy baseline scored higher"

        content = (
            "SELECTED CITY VISIT ORDER:\n"
            + " -> ".join(result["order"])
            + "\n\nFULL RAIL PATH (including interchange cities):\n"
            + " -> ".join(stats["full_path"])
            + f"\n\nTotal estimated time: {stats['time']:.1f} hours"
            + f"\nCumulative scenic score: {stats['scenic']:.0f}"
            + f"\nEstimated train changes: {stats['changes']}"
            + f"\nGenetic algorithm fitness: {ga_score:.2f}"
            + f"\nGreedy baseline fitness: {greedy_score:.2f}"
            + f"\n\n{verdict}."
            + "\nHigher fitness (closer to zero) means a better weighted route."
        )

        output = tk.Text(
            popup,
            font=("Helvetica", 11),
            bg=self.theme["surface"],
            fg=self.theme["text"],
            relief="flat",
            wrap="word",
            height=20
        )

        output.pack(fill="both", expand=True, padx=24, pady=12)
        output.insert("1.0", content)
        output.configure(state="disabled")

        self.button(popup, "Close", popup.destroy, width=16, pady=(0, 12))

    def display_graphs(self):
        if self.result is None:
            messagebox.showerror("No results yet", "Run the optimiser before displaying graphs")
            return

        stats = self.result["stats"]
        optimizer = self.result["optimizer"]

        # Graph 1: Journey statistics
        plt.figure()
        plt.bar(["Travel hours", "Scenic score", "Changes"], [stats["time"], stats["scenic"], stats["changes"]])
        plt.title("Modelled journey summary (different units)")
        plt.ylabel("Value")
        plt.tight_layout()

        # graph 2: Genetic algorithm improvement
        plt.figure()
        plt.plot(optimizer.best_scores, label="Best fitness")
        plt.plot(optimizer.mean_scores, label="Mean fitness")
        plt.title("Genetic algorithm performance")
        plt.xlabel("Generation")
        plt.ylabel("Fitness (higher is better)")
        plt.legend()
        plt.tight_layout()

        plt.show()


# MAIN PROGRAM

def main():
    filename = Path(__file__).with_name("routes.csv")

    try:
        network = RailNetwork(filename)
    except (OSError, ValueError) as error:
        print("Could not load routes.csv:", error)
        return

    root = tk.Tk()
    InterraillerApp(root, network)
    root.mainloop()


if __name__ == "__main__":
    main()
