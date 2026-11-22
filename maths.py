import numpy as np
import matplotlib.pyplot as plt

# Measurements from the toothpaste tube
front_width = np.array([
    5.30, 5.10, 4.95, 4.80, 4.65, 4.50, 4.35,
    4.20, 4.05, 3.90, 3.75, 3.60, 3.45
])

side_depth = np.array([
    0.00, 0.50, 0.90, 1.35, 1.50, 1.80, 2.00,
    2.25, 2.45, 2.65, 2.90, 3.10, 3.20
])

# The tube body is 8.8 cm long and has 13 measured points
tube_length = 8.8
x = np.linspace(0, tube_length, 13)

# Create the graph
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(
    x,
    front_width,
    marker="o",
    linewidth=2,
    markersize=7,
    label=r"Front width $W_k$"
)

ax.plot(
    x,
    side_depth,
    marker="o",
    linewidth=2,
    markersize=7,
    label=r"Side depth $D_k$"
)

# Axis labels
ax.set_xlabel(r"Distance along tube body, $x$ (cm)", fontsize=12)
ax.set_ylabel("Measured dimension (cm)", fontsize=12)

# Formatting
ax.grid(True, alpha=0.3)
ax.legend(fontsize=11)
ax.tick_params(axis="both", labelsize=11)

# Leave space beneath the graph for the figure caption
fig.subplots_adjust(bottom=0.22)

fig.text(
    0.5,
    0.06,
    "Figure 2. Measured front width and side depth along the tube body.",
    ha="center",
    fontsize=11,
    fontstyle="italic",
    fontweight="bold"
)

# Save a high-resolution copy for the IA
plt.savefig(
    "toothpaste_measurements_graph.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()