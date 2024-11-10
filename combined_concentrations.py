import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

# Parameters for the Gaussian function
Q = 6 * 10**12  # Total quantity
background = 8e14  # Value to move the function up
diffusions_gaussian = [2.5623102476e-14, 2.970263357e-13, 9.1373436904e-14]
times_gaussian = [90 * 60, 60 * 60, 37 * 60]
colors_gaussian = ["blue", "orange", "red", "purple"]
labels_gaussian = [
    "Boron Ion Implant",
    "After Field Oxide",
    "After Gate Oxide",
    "Boron After Intermediate Oxide",
]

# Parameters for the Drive-in function
N0 = 10e21  # Solid solubility limit
diffusions_drivein = [9.1373436904e-14, 9.1373436904e-14]
times_drivein = [10 * 60, 37 * 60]
colors_drivein = ["green", "magenta"]
labels_drivein = ["Diffusion", "Phosphorous After Drive-in"]

# Define the Gaussian function
def gaussian_N(x, N1, R, R1):
    return N1 * np.exp(-((x - R) ** 2) / (2 * R1**2))

# Define the Drive-in functions
def const_source_N(x, N0, D, t):
    return N0 * erfc(x / (2 * np.sqrt(D * t)))

def limited_source_N(x, Q, D, t):
    return (Q / np.sqrt(D * t * np.pi)) * np.exp(-x**2 / (4 * D * t))

# Parameters for the "After Intermediate Oxide" Gaussian
delta_Rp = 4 * 10**-6
Rp = 2 * 10**-5
for i in range(3):
    delta_Rp = np.sqrt(delta_Rp**2 + 2 * diffusions_gaussian[i] * times_gaussian[i])
Np = Q / (np.sqrt(2 * np.pi) * delta_Rp)

# Generate x values centered around Rp
x_min = Rp - 10 * delta_Rp
x_max = Rp + 10 * delta_Rp
x_gaussian = np.linspace(x_min, x_max, 500)

# Gaussian shifted with background
y_gaussian = gaussian_N(x_gaussian, Np, Rp, delta_Rp)
y_gaussian_shifted = y_gaussian + background

# Plot the "After Intermediate Oxide" Gaussian
plt.figure(figsize=(8, 6))
plt.axhline(y=background, color="green", linestyle="--", label="Background Concentration")
plt.plot(x_gaussian, y_gaussian_shifted, label=labels_gaussian[3], color=colors_gaussian[3])

# Add the "Drive-in" graph
for i in range(2):
    # x_drivein = np.linspace(0, 0.00002, 500)
    if i == 0:
        y_drivein = const_source_N(x_gaussian, N0, diffusions_drivein[i], times_drivein[i])
        Q_drivein = 2 * N0 * np.sqrt((diffusions_drivein[i] * times_drivein[i]) / np.pi)
    else:
        y_drivein = limited_source_N(x_gaussian, Q_drivein, diffusions_drivein[i], times_drivein[i])
        plt.plot(x_gaussian, y_drivein, label=labels_drivein[i], color=colors_drivein[i])
        print(np.max(y_drivein))

# Set y-axis to log scale
plt.yscale("log")

# Add labels, title, and grid
plt.title("Overlay of Gaussian and Drive-in Concentration Profiles", fontsize=16)
plt.xlabel("x (cm)", fontsize=14)
plt.ylabel("Log(Concentration)", fontsize=14)
plt.xlim(0)
plt.ylim(10**14, 10**19)
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.legend(fontsize=12)

# Save and show the plot
plt.savefig("/Users/karimel-refai/classes/ee143/lab_report1/combined_concentrations.png")
plt.show()
