import tkinter as tk
from tkinter import ttk
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ============================================================
# TMUA GRAPH FLASHCARDS — EQUATION <-> GRAPH TRAINER
#
# Install once in the PyCharm terminal:
#   pip install numpy matplotlib
#
# Controls:
#   Space = reveal
#   Right arrow = next
#   Left arrow = previous
#   G = mark "Got it"
#   M = mark "Missed"
#   R = reshuffle
# ============================================================


def card(name, latex, func, xlim=(-6, 6), ylim=(-6, 6),
         category="Core", difficulty="Easy", notes="", clip=20):
    return {
        "name": name,
        "latex": latex,
        "func": func,
        "xlim": xlim,
        "ylim": ylim,
        "category": category,
        "difficulty": difficulty,
        "notes": notes,
        "clip": clip,
    }


def safe_sqrt(x):
    return np.where(x >= 0, np.sqrt(np.maximum(x, 0)), np.nan)


def safe_log(x):
    return np.where(x > 0, np.log(x), np.nan)


def safe_log_abs(x):
    return np.where(np.abs(x) > 1e-8, np.log(np.abs(x)), np.nan)


def sinc(x):
    return np.sinc(x / np.pi)


CARDS = [
    # ===================== EASY =====================
    card("Square root", r"$y=\sqrt{x}$",
         safe_sqrt, (0, 9), (-1, 4), "Core", "Easy",
         "Domain x≥0. Starts at (0,0). Increasing with decreasing gradient."),

    card("Absolute value", r"$y=|x|$",
         np.abs, (-6, 6), (-1, 6), "Core", "Easy",
         "Even function. V-shape with a corner at the origin."),

    card("Quadratic", r"$y=x^2$",
         lambda x: x**2, (-4, 4), (-1, 10), "Core", "Easy",
         "Even. Minimum at (0,0)."),

    card("Negative quadratic", r"$y=-x^2$",
         lambda x: -(x**2), (-4, 4), (-10, 1), "Core", "Easy",
         "Reflection of x² in the x-axis."),

    card("Cubic", r"$y=x^3$",
         lambda x: x**3, (-2.2, 2.2), (-8, 8), "Core", "Easy",
         "Odd. Stationary point of inflection at the origin."),

    card("Cube root", r"$y=\sqrt[3]{x}$",
         np.cbrt, (-8, 8), (-3, 3), "Core", "Easy",
         "Inverse of x³. Odd and very steep near x=0."),

    card("Reciprocal", r"$y=\frac1x$",
         lambda x: 1/x, (-6, 6), (-6, 6), "Core", "Easy",
         "Odd. Asymptotes x=0 and y=0.", 10),

    card("Reciprocal squared", r"$y=\frac1{x^2}$",
         lambda x: 1/(x**2), (-6, 6), (-1, 8), "Core", "Easy",
         "Even, always positive. Asymptotes x=0 and y=0.", 12),

    card("Exponential", r"$y=e^x$",
         np.exp, (-4, 3), (-1, 10), "Exp / log", "Easy",
         "Always positive. Passes through (0,1). Horizontal asymptote y=0."),

    card("Logarithm", r"$y=\ln x$",
         safe_log, (0.05, 8), (-4, 3), "Exp / log", "Easy",
         "Domain x>0. Vertical asymptote x=0. Passes through (1,0)."),

    card("Sine", r"$y=\sin x$",
         np.sin, (-2*np.pi, 2*np.pi), (-1.5, 1.5), "Trig", "Easy",
         "Odd. Period 2π. Zeros at nπ."),

    card("Cosine", r"$y=\cos x$",
         np.cos, (-2*np.pi, 2*np.pi), (-1.5, 1.5), "Trig", "Easy",
         "Even. Period 2π. y(0)=1."),

    card("Tangent", r"$y=\tan x$",
         np.tan, (-2*np.pi, 2*np.pi), (-6, 6), "Trig", "Easy",
         "Odd. Period π. Vertical asymptotes at π/2+nπ.", 8),

    # ===================== MEDIUM =====================
    card("Shifted square root", r"$y=\sqrt{x-2}+1$",
         lambda x: np.where(x >= 2, np.sqrt(np.maximum(x - 2, 0)) + 1, np.nan),
         (-1, 10), (-1, 5), "Transformations", "Medium",
         "√x shifted 2 right and 1 up. Endpoint is (2,1)."),

    card("Shifted absolute value", r"$y=|x-2|-1$",
         lambda x: np.abs(x - 2) - 1, (-4, 8), (-3, 7),
         "Transformations", "Medium",
         "Vertex at (2,-1)."),

    card("Reflected shifted quadratic", r"$y=-(x-2)^2+3$",
         lambda x: -(x - 2)**2 + 3, (-3, 7), (-7, 5),
         "Transformations", "Medium",
         "Maximum at (2,3)."),

    card("Double-angle sine", r"$y=\sin(2x)$",
         lambda x: np.sin(2*x), (-2*np.pi, 2*np.pi), (-1.5, 1.5),
         "Trig", "Medium",
         "Amplitude 1. Period π."),

    card("Half-angle cosine", r"$y=\cos\left(\frac{x}{2}\right)$",
         lambda x: np.cos(x/2), (-4*np.pi, 4*np.pi), (-1.5, 1.5),
         "Trig", "Medium",
         "Period 4π. Horizontal stretch by factor 2."),

    card("Squared sine", r"$y=\sin^2x$",
         lambda x: np.sin(x)**2, (-2*np.pi, 2*np.pi), (-0.3, 1.3),
         "Trig", "Medium",
         "Always non-negative. Period π. Equals (1-cos2x)/2."),

    card("Absolute sine", r"$y=|\sin x|$",
         lambda x: np.abs(np.sin(x)), (-2*np.pi, 2*np.pi), (-0.3, 1.3),
         "Trig", "Medium",
         "Reflect negative parts of sin x upward. Period π."),

    card("Simple rational", r"$y=\frac{x}{x^2+1}$",
         lambda x: x/(x**2 + 1), (-7, 7), (-1.2, 1.2),
         "Rational", "Medium",
         "Odd. Tends to 0. Turning points at x=±1."),

    card("Parabola reciprocal", r"$y=\frac1{x^2+1}$",
         lambda x: 1/(x**2 + 1), (-6, 6), (-0.2, 1.2),
         "Rational", "Medium",
         "Even. Maximum 1 at x=0. No vertical asymptote."),

    card("Rational approaches one", r"$y=\frac{x^2}{x^2+1}$",
         lambda x: x**2/(x**2 + 1), (-6, 6), (-0.2, 1.2),
         "Rational", "Medium",
         "Even. Minimum 0. Horizontal asymptote y=1."),

    card("Log absolute", r"$y=\ln|x|$",
         safe_log_abs, (-8, 8), (-4, 3),
         "Exp / log", "Medium",
         "Even. Vertical asymptote x=0. Zeros at ±1."),

    card("Exponential decay", r"$y=e^{-x}$",
         lambda x: np.exp(-x), (-3, 4), (-1, 10),
         "Exp / log", "Medium",
         "Reflection of e^x in the y-axis."),

    card("Gaussian", r"$y=e^{-x^2}$",
         lambda x: np.exp(-(x**2)), (-4, 4), (-0.2, 1.3),
         "Exp / log", "Medium",
         "Even bell shape. Maximum 1 at x=0."),

    card("Product trig", r"$y=\sin x\cos x$",
         lambda x: np.sin(x)*np.cos(x),
         (-2*np.pi, 2*np.pi), (-0.8, 0.8),
         "Trig", "Medium",
         "Use sin x cos x = ½sin(2x)."),

    card("Sine plus second harmonic", r"$y=\sin x+\sin(2x)$",
         lambda x: np.sin(x) + np.sin(2*x),
         (-2*np.pi, 2*np.pi), (-2.5, 2.5),
         "Trig", "Medium",
         "Combination of two frequencies. Overall period 2π."),

    card("Absolute quadratic", r"$y=|x^2-4|$",
         lambda x: np.abs(x**2 - 4),
         (-4, 4), (-1, 10),
         "Transformations", "Medium",
         "Reflect any part of x²-4 below the x-axis upward."),

    card("Root of absolute x", r"$y=\sqrt{|x|}$",
         lambda x: np.sqrt(np.abs(x)),
         (-9, 9), (-1, 4),
         "Transformations", "Medium",
         "Even. Mirror √x into the left half-plane."),

    card("Nested absolute", r"$y=||x|-2|$",
         lambda x: np.abs(np.abs(x) - 2),
         (-6, 6), (-1, 5),
         "Transformations", "Medium",
         "Even W-shape. Zeros at x=±2."),

    card("Piecewise-looking sum", r"$y=|x|+|x-2|$",
         lambda x: np.abs(x) + np.abs(x-2),
         (-4, 6), (0, 10),
         "Transformations", "Medium",
         "Flat between x=0 and x=2, where the sum equals 2."),

    # ===================== EVIL =====================
    card("Two vertical asymptotes", r"$y=\frac1{x^2-1}$",
         lambda x: 1/(x**2 - 1),
         (-5, 5), (-6, 6),
         "Rational", "Evil",
         "Even. Vertical asymptotes x=±1. Horizontal asymptote y=0.", 10),

    card("Oblique asymptote", r"$y=x+\frac1x$",
         lambda x: x + 1/x,
         (-6, 6), (-8, 8),
         "Rational", "Evil",
         "Vertical asymptote x=0. Oblique asymptote y=x.", 15),

    card("Removable hole", r"$y=\frac{x^2-1}{x-1}$",
         lambda x: np.where(
             np.abs(x-1) > 1e-5,
             (x**2 - 1)/(x - 1),
             np.nan
         ),
         (-5, 5), (-5, 7),
         "Rational", "Evil",
         "Same as y=x+1 except x=1 is missing: a hole at (1,2)."),

    card("Absolute reciprocal shift", r"$y=\frac1{|x|-1}$",
         lambda x: 1/(np.abs(x) - 1),
         (-6, 6), (-6, 6),
         "Rational", "Evil",
         "Even. Vertical asymptotes at x=±1.", 10),

    card("Logistic", r"$y=\frac1{1+e^{-x}}$",
         lambda x: 1/(1 + np.exp(-x)),
         (-8, 8), (-0.2, 1.2),
         "Exp / log", "Evil",
         "S-curve. Horizontal asymptotes y=0 and y=1. y(0)=1/2."),

    card("Sine of cosine", r"$y=\sin(\cos x)$",
         lambda x: np.sin(np.cos(x)),
         (-2*np.pi, 2*np.pi), (-1.1, 1.1),
         "Composites", "Evil",
         "Even. Since cos x∈[-1,1], range is [-sin1,sin1]."),

    card("Cosine of sine", r"$y=\cos(\sin x)$",
         lambda x: np.cos(np.sin(x)),
         (-2*np.pi, 2*np.pi), (0.45, 1.1),
         "Composites", "Evil",
         "Never negative. Range [cos1,1]. Period π."),

    card("Sine of a square", r"$y=\sin(x^2)$",
         lambda x: np.sin(x**2),
         (-4, 4), (-1.3, 1.3),
         "Composites", "Evil",
         "Even. Oscillations become more frequent as |x| grows."),

    card("x times sine", r"$y=x\sin x$",
         lambda x: x*np.sin(x),
         (-3*np.pi, 3*np.pi), (-10, 10),
         "Composites", "Evil",
         "Even because odd×odd. Envelopes are y=±|x|."),

    card("Sinc", r"$y=\frac{\sin x}{x}$",
         sinc,
         (-5*np.pi, 5*np.pi), (-0.4, 1.2),
         "Composites", "Evil",
         "Even. Limit at x=0 is 1. Oscillations decay toward 0."),

    card("Sine of reciprocal", r"$y=\sin\left(\frac1x\right)$",
         lambda x: np.where(
             np.abs(x) > 1e-5,
             np.sin(1/x),
             np.nan
         ),
         (-2, 2), (-1.3, 1.3),
         "Composites", "Evil",
         "Undefined at x=0. Oscillates increasingly rapidly near x=0.", 3),

    card("Damped oscillation", r"$y=e^{-0.3x}\sin x$",
         lambda x: np.exp(-0.3*x)*np.sin(x),
         (0, 14), (-1.2, 1.2),
         "Composites", "Evil",
         "Oscillates inside envelopes ±e^{-0.3x}."),

    card("Cusp power", r"$y=|x|^{2/3}$",
         lambda x: np.abs(x)**(2/3),
         (-6, 6), (-1, 4),
         "Composites", "Evil",
         "Even. Sharp cusp/vertical-tangent behaviour at the origin."),

    card("Min of two parabolas", r"$y=\min(x^2,(x-2)^2)$",
         lambda x: np.minimum(x**2, (x-2)**2),
         (-3, 5), (-1, 10),
         "Composites", "Evil",
         "Take whichever parabola is lower. They switch at x=1."),

    card("Cosine after square root", r"$y=\cos(\sqrt{|x|})$",
         lambda x: np.cos(np.sqrt(np.abs(x))),
         (-20, 20), (-1.3, 1.3),
         "Composites", "Evil",
         "Even. Oscillations spread farther apart as |x| increases."),

    card("Absolute rational", r"$y=\left|\frac{x-1}{x+1}\right|$",
         lambda x: np.abs((x-1)/(x+1)),
         (-6, 6), (-0.5, 6),
         "Rational", "Evil",
         "Vertical asymptote x=-1. Zero at x=1. Horizontal asymptote y=1.", 10),
]


class GraphFlashcards:
    def __init__(self, root):
        self.root = root
        self.root.title("TMUA Graph Flashcards")
        self.root.geometry("1050x820")
        self.root.minsize(820, 650)

        self.filtered_cards = []
        self.order = []
        self.pos = 0
        self.revealed = False

        self.got = 0
        self.missed = 0
        self.answered_current = False

        # ================= TOP BAR =================
        top = ttk.Frame(root, padding=(12, 10, 12, 4))
        top.pack(fill="x")

        ttk.Label(top, text="Mode:").pack(side="left")

        self.mode_var = tk.StringVar(value="Equation → Graph")

        self.mode_box = ttk.Combobox(
            top,
            textvariable=self.mode_var,
            values=[
                "Equation → Graph",
                "Graph → Equation"
            ],
            state="readonly",
            width=19
        )

        self.mode_box.pack(side="left", padx=(6, 14))

        self.mode_box.bind(
            "<<ComboboxSelected>>",
            lambda e: self.show_front()
        )

        ttk.Label(top, text="Difficulty:").pack(side="left")

        self.difficulty_var = tk.StringVar(value="All")

        self.difficulty_box = ttk.Combobox(
            top,
            textvariable=self.difficulty_var,
            values=[
                "All",
                "Easy",
                "Medium",
                "Evil"
            ],
            state="readonly",
            width=10
        )

        self.difficulty_box.pack(side="left", padx=(6, 14))

        self.difficulty_box.bind(
            "<<ComboboxSelected>>",
            lambda e: self.reset_deck()
        )

        ttk.Label(top, text="Topic:").pack(side="left")

        categories = ["All"] + sorted({
            c["category"] for c in CARDS
        })

        self.category_var = tk.StringVar(value="All")

        self.category_box = ttk.Combobox(
            top,
            textvariable=self.category_var,
            values=categories,
            state="readonly",
            width=17
        )

        self.category_box.pack(side="left", padx=(6, 10))

        self.category_box.bind(
            "<<ComboboxSelected>>",
            lambda e: self.reset_deck()
        )

        ttk.Button(
            top,
            text="Shuffle",
            command=self.shuffle_deck
        ).pack(side="left", padx=4)

        self.progress_label = ttk.Label(top, text="")
        self.progress_label.pack(side="right")

        # ================= GRAPH =================
        self.fig, self.ax = plt.subplots(
            figsize=(8.8, 5.35),
            dpi=100
        )

        self.fig.subplots_adjust(
            left=0.09,
            right=0.97,
            bottom=0.12,
            top=0.88
        )

        self.canvas = FigureCanvasTkAgg(
            self.fig,
            master=root
        )

        self.canvas.get_tk_widget().pack(
            fill="both",
            expand=True,
            padx=12,
            pady=6
        )

        # ================= NOTES =================
        self.notes_var = tk.StringVar(value="")

        self.notes_label = ttk.Label(
            root,
            textvariable=self.notes_var,
            anchor="center",
            justify="center",
            wraplength=900,
            font=("TkDefaultFont", 11)
        )

        self.notes_label.pack(
            fill="x",
            padx=20,
            pady=(2, 8)
        )

        # ================= SCORE =================
        rating = ttk.Frame(
            root,
            padding=(12, 0, 12, 4)
        )

        rating.pack(fill="x")

        self.score_label = ttk.Label(
            rating,
            text="Score: 0 correct • 0 missed"
        )

        self.score_label.pack(side="left")

        self.got_button = ttk.Button(
            rating,
            text="Got it  [G]",
            command=lambda: self.rate(True),
            state="disabled"
        )

        self.got_button.pack(
            side="right",
            padx=(6, 0)
        )

        self.missed_button = ttk.Button(
            rating,
            text="Missed  [M]",
            command=lambda: self.rate(False),
            state="disabled"
        )

        self.missed_button.pack(side="right")

        # ================= NAVIGATION =================
        buttons = ttk.Frame(
            root,
            padding=(12, 4, 12, 12)
        )

        buttons.pack(fill="x")

        ttk.Button(
            buttons,
            text="← Previous",
            command=self.previous_card
        ).pack(side="left")

        self.reveal_button = ttk.Button(
            buttons,
            text="Reveal",
            command=self.reveal
        )

        self.reveal_button.pack(
            side="left",
            expand=True,
            padx=12,
            ipadx=35,
            ipady=6
        )

        ttk.Button(
            buttons,
            text="Next →",
            command=self.next_card
        ).pack(side="right")

        # ================= KEYBOARD SHORTCUTS =================
        root.bind("<space>", self.on_space)

        root.bind(
            "<Right>",
            lambda e: self.next_card()
        )

        root.bind(
            "<Left>",
            lambda e: self.previous_card()
        )

        root.bind(
            "g",
            lambda e: self.rate(True)
        )

        root.bind(
            "m",
            lambda e: self.rate(False)
        )

        root.bind(
            "r",
            lambda e: self.shuffle_deck()
        )

        self.reset_deck()

    # =========================================================
    # DECK MANAGEMENT
    # =========================================================

    def reset_deck(self):
        chosen_cat = self.category_var.get()
        chosen_diff = self.difficulty_var.get()

        cards = list(CARDS)

        if chosen_cat != "All":
            cards = [
                c for c in cards
                if c["category"] == chosen_cat
            ]

        if chosen_diff != "All":
            cards = [
                c for c in cards
                if c["difficulty"] == chosen_diff
            ]

        self.filtered_cards = cards

        self.order = list(
            range(len(cards))
        )

        random.shuffle(self.order)

        self.pos = 0

        self.got = 0
        self.missed = 0

        self.update_score()

        if self.filtered_cards:
            self.show_front()

        else:
            self.ax.clear()
            self.ax.set_axis_off()

            self.ax.text(
                0.5,
                0.5,
                "No cards match those filters.",
                ha="center",
                va="center",
                transform=self.ax.transAxes,
                fontsize=18
            )

            self.canvas.draw_idle()

            self.notes_var.set("")
            self.progress_label.config(
                text="0 / 0"
            )

    def shuffle_deck(self):
        if not self.order:
            return

        random.shuffle(self.order)

        self.pos = 0

        self.show_front()

    def current_card(self):
        return self.filtered_cards[
            self.order[self.pos]
        ]

    # =========================================================
    # SCORE
    # =========================================================

    def update_score(self):
        self.score_label.config(
            text=(
                f"Score: {self.got} correct "
                f"• {self.missed} missed"
            )
        )

    def rate(self, correct):
        if not self.revealed:
            return

        if self.answered_current:
            return

        self.answered_current = True

        if correct:
            self.got += 1
        else:
            self.missed += 1

        self.update_score()

        self.got_button.config(
            state="disabled"
        )

        self.missed_button.config(
            state="disabled"
        )

    # =========================================================
    # GRAPH DRAWING
    # =========================================================

    def style_axes(self, c):
        self.ax.set_xlim(
            *c["xlim"]
        )

        self.ax.set_ylim(
            *c["ylim"]
        )

        self.ax.axhline(
            0,
            linewidth=0.9
        )

        self.ax.axvline(
            0,
            linewidth=0.9
        )

        self.ax.grid(
            True,
            alpha=0.20
        )

        self.ax.set_xlabel("x")

        self.ax.set_ylabel(
            "y",
            rotation=0,
            labelpad=12
        )

    def get_xy(self, c):
        xmin, xmax = c["xlim"]

        x = np.linspace(
            xmin,
            xmax,
            6000
        )

        with np.errstate(all="ignore"):
            y = np.asarray(
                c["func"](x),
                dtype=float
            )

        # remove invalid values
        y[~np.isfinite(y)] = np.nan

        # hide absurd values near asymptotes
        y[np.abs(y) > c["clip"]] = np.nan

        # Stop matplotlib from joining two sides
        # of a vertical asymptote.
        finite_pairs = (
            np.isfinite(y[:-1])
            &
            np.isfinite(y[1:])
        )

        jump_threshold = max(
            4.0,
            (
                c["ylim"][1]
                -
                c["ylim"][0]
            ) * 0.65
        )

        bad = np.where(
            finite_pairs
            &
            (
                np.abs(
                    np.diff(y)
                )
                >
                jump_threshold
            )
        )[0]

        y[bad + 1] = np.nan

        return x, y

    def draw_graph(
        self,
        c,
        show_title=False
    ):
        self.ax.clear()

        x, y = self.get_xy(c)

        self.ax.plot(
            x,
            y,
            linewidth=2.2
        )

        self.style_axes(c)

        if show_title:
            self.ax.set_title(
                c["latex"],
                fontsize=20,
                pad=12
            )

        else:
            self.ax.set_title(
                "Which equation gives this graph?",
                fontsize=16,
                pad=12
            )

    # =========================================================
    # FLASHCARD DISPLAY
    # =========================================================

    def show_front(self):
        if not self.filtered_cards:
            return

        c = self.current_card()

        self.revealed = False
        self.answered_current = False

        self.got_button.config(
            state="disabled"
        )

        self.missed_button.config(
            state="disabled"
        )

        self.progress_label.config(
            text=(
                f"{self.pos + 1} / "
                f"{len(self.order)} "
                f" • {c['difficulty']} "
                f" • {c['category']}"
            )
        )

        mode = self.mode_var.get()

        # ------------------------------------------------------
        # EQUATION -> GRAPH
        # ------------------------------------------------------

        if mode == "Equation → Graph":

            self.ax.clear()
            self.ax.set_axis_off()

            self.ax.text(
                0.5,
                0.59,
                c["latex"],
                transform=self.ax.transAxes,
                ha="center",
                va="center",
                fontsize=30
            )

            self.ax.text(
                0.5,
                0.36,
                (
                    "Predict: shape • intercepts • "
                    "symmetry • asymptotes • range"
                ),
                transform=self.ax.transAxes,
                ha="center",
                va="center",
                fontsize=11,
                alpha=0.70
            )

            self.reveal_button.config(
                text="Reveal graph"
            )

            self.notes_var.set(
                "Try to sketch it mentally before revealing."
            )

        # ------------------------------------------------------
        # GRAPH -> EQUATION
        # ------------------------------------------------------

        else:

            self.draw_graph(
                c,
                show_title=False
            )

            self.reveal_button.config(
                text="Reveal equation"
            )

            self.notes_var.set(
                "Guess the equation before revealing."
            )

        self.canvas.draw_idle()

    def reveal(self):
        if not self.filtered_cards:
            return

        if self.revealed:
            return

        c = self.current_card()

        self.revealed = True

        mode = self.mode_var.get()

        if mode == "Equation → Graph":

            self.draw_graph(
                c,
                show_title=True
            )

        else:

            self.ax.set_title(
                c["latex"],
                fontsize=20,
                pad=12
            )

        self.notes_var.set(
            c["notes"]
        )

        self.reveal_button.config(
            text="Revealed"
        )

        self.got_button.config(
            state="normal"
        )

        self.missed_button.config(
            state="normal"
        )

        self.canvas.draw_idle()

    # =========================================================
    # NAVIGATION
    # =========================================================

    def next_card(self):
        if not self.order:
            return

        self.pos = (
            self.pos + 1
        ) % len(self.order)

        self.show_front()

    def previous_card(self):
        if not self.order:
            return

        self.pos = (
            self.pos - 1
        ) % len(self.order)

        self.show_front()

    def on_space(self, event):

        focused = self.root.focus_get()

        if focused in (
            self.mode_box,
            self.difficulty_box,
            self.category_box
        ):
            return

        self.reveal()

        return "break"


# ============================================================
# RUN PROGRAM
# ============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = GraphFlashcards(root)

    root.mainloop()