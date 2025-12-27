def calculate_beam_deflection(L, E, I_b, P):
    import numpy as np

    x = np.linspace(0, L, 100)
    v = (P / (6 * E * I_b)) * x**2 * (3 * L - x)
    max_def = v[-1]
    return x, v, max_def


def plot_results(x, v):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 6))
    plt.plot(x, v * 1000, "b-", linewidth=2)
    plt.xlabel("Position (m)")
    plt.ylabel("Deflection (mm)")
    plt.title("Beam Deflection")
    plt.grid(True, alpha=0.3)
    plt.show()


# Call functions
L = 10.0
E = 200e9
I_b = 8.33e-6
P = 1000
x, v, max_def = calculate_beam_deflection(L, E, I_b, P)
plot_results(x, v)
print(f"Max deflection: {max_def*1000:.2f} mm")
