import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

# Parameters for the function
N0 = 10e21 # Solid solubility limit
diffusions = [2.5623102476e-14, 2.970263357e-13, 9.1373436904e-14]            # Time differences
times = [10 * 60 , 37 * 60]  # Time values
colors = ["blue", "orange"]
labels = ["Diffusion", "Drive-in"]               # Labels for the plot
# Define the function
def const_source_N(x, N0, D, t):
    return N0 * erfc(x / (2 * np.sqrt(D * t)))

def limited_source_N(x, Q, D, t):
    print(Q, D, t)
    return (Q / np.sqrt(D * t * np.pi)) * np.exp(-x**2 / (4 * D * t))


# Plot the function
plt.figure(figsize=(8, 6))

for i in range(2):
    x_min = 0
    x_max = 0.00002
    x = np.linspace(x_min, x_max, 500)
    if i == 0:
        # use const
        y = const_source_N(x, N0, diffusions[i], times[i])
        Q = 2 * N0 * np.sqrt((diffusions[i] * times[i])/np.pi)
    else: 
        # use limited source
        # Q1 = 2 * N1 * np.sqrt((diffusions[0] * times[0])/np.pi)
        y = limited_source_N(x, Q, diffusions[i], times[i]) 
    # x_min = 0
    # x_max = 1.0
    # x = np.linspace(x_min, x_max, 500)
    print(np.max(y))
    plt.plot(x, y, label=labels[i], color=colors[i])

# Set the y-axis to log scale
plt.yscale('log')

# Add labels and title
plt.title("Concentration of P Across Fabrication Steps", fontsize=16)
plt.xlabel("x (cm)", fontsize=14)
plt.ylabel("Log(Concentration P)", fontsize=14)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend(fontsize=12)

# Show the plot
plt.savefig("/Users/karimel-refai/classes/ee143/lab_report1/p_concentrations.png")
plt.show()

