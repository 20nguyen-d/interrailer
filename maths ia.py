import numpy as np
import math
import scipy
from scipy.integrate import dblquad

# Measurements from your tube
W = np.array([5.3, 5.1, 4.95, 4.8, 4.65, 4.5, 4.35, 4.2, 4.05, 3.9, 3.75, 3.6, 3.45])
D = np.array([0, 0.5, 0.9, 1.35, 1.5, 1.8, 2, 2.25, 2.45, 2.65, 2.9, 3.1, 3.2])

# Total tube length
L = 8.8

# Distance between rings
s = L / 12

# Convert full width/depth into semi-axes
a = W / 2
b = D / 2

band_areas = []

for k in range(12):
    # Starting and ending semi-axes for band k
    a_k = a[k]
    a_next = a[k + 1]

    b_k = b[k]
    b_next = b[k + 1]


    # Linear interpolation functions:
    # a_func(t) = semi-width at distance t through the band
    # b_func(t) = semi-depth at distance t through the band

    def a_func(t):
        return a_k + ((a_next - a_k) / s) * t


    def b_func(t):
        return b_k + ((b_next - b_k) / s) * t


    # Derivatives of a_func(t) and b_func(t)
    def a_prime(t):
        return (a_next - a_k) / s


    def b_prime(t):
        return (b_next - b_k) / s


    # Integrand from the surface area formula
    def integrand(v, t):
        a_t = a_func(t)
        b_t = b_func(t)
        ap_t = a_prime(t)
        bp_t = b_prime(t)

        return math.sqrt(
            (ap_t * b_t * math.cos(v) ** 2 + bp_t * a_t * math.sin(v) ** 2) ** 2
            + b_t ** 2 * math.cos(v) ** 2
            + a_t ** 2 * math.sin(v) ** 2
        )


    # Surface area of band k
    # t goes from 0 to s
    # v goes from 0 to 2pi
    area, error = dblquad(
        integrand,
        0, s,
        lambda t: 0,
        lambda t: 2 * math.pi
    )

    band_areas.append(area)

# Print results
total_surface_area = sum(band_areas)

print("Band surface areas:")
for i, area in enumerate(band_areas, start=1):
    print(f"Band {i}: {area:.4f} cm^2")

print()
print(f"Total surface area: {total_surface_area:.4f} cm^2")
print(f"Total surface area to 3 s.f.: {total_surface_area:.3g} cm^2")













