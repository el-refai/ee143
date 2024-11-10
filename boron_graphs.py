import numpy as np
import matplotlib.pyplot as plt

# Parameters for the function
Q = 6 * 10**12                  # Total quantity
background = 8e14               # Value to move the function up
diffusions = [2.5623102476e-14, 2.970263357e-13, 9.1373436904e-14, 9.1373436904e-14]  # Time differences
times = [90 * 60, 60 * 60, 10*60, 37 * 60]  # Time values
colors = ["blue", "orange", "red", "purple", "magenta"]  # Colors for the plot
labels = ["Boron Ion Implant", "After Field Oxide", "After Gate Oxide", "After Diffusion", "After Intermediate Oxide"]  # Labels for the plot

# Define the function
def N(x, N1, R, R1):
    return N1 * np.exp(-((x - R) ** 2) / (2 * R1 ** 2))

# Plot the first Gaussian
plt.figure(figsize=(8, 6))
delta_Rp = 4 * 10**-6
Rp = 2 * 10**-5
Np = (Q / (np.sqrt(2 * np.pi) * delta_Rp))
x_min = Rp - 10 * delta_Rp # 0
x_max = Rp + 10 * delta_Rp
x = np.linspace(x_min, x_max, 500)
y = N(x, Np, Rp, delta_Rp)
y_shifted = y + background
plt.axhline(y=background, color='green', linestyle='--', label="Background Concentration")
plt.plot(x, y_shifted, label=labels[0], color=colors[0])
plt.yscale('log')
plt.title("Concentration of B11 - Boron Ion Implant", fontsize=16)
plt.xlabel("x (cm)", fontsize=14)
plt.xlim(0)
plt.ylabel("Log(Concentration B11)", fontsize=14)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend(fontsize=12)
plt.savefig("/Users/karimel-refai/classes/ee143/lab_report1/B_concentration_first.png")
plt.close()

# Plot the remaining Gaussians
plt.figure(figsize=(8, 6))
plt.axhline(y=background, color='green', linestyle='--', label="Background Concentration")
delta_Rp = 4 * 10**-6
Rp = 2 * 10**-5
for i in range(1, 5):
    delta_Rp = np.sqrt(delta_Rp ** 2 + 2 * diffusions[i-1] * times[i-1])
    Np = (Q / (np.sqrt(2 * np.pi) * delta_Rp))
    if i == 1:
        x_min = Rp - 15 * delta_Rp
        x_max = Rp + 15 * delta_Rp
        x = np.linspace(x_min, x_max, 500)
    if i == 4:
        print(Np, Rp, delta_Rp)
    y = N(x, Np, Rp, delta_Rp)
    y_shifted = y + background
    plt.plot(x, y_shifted, label=labels[i], color=colors[i])
plt.yscale('log')
plt.title("Concentration of B11 - Subsequent Steps", fontsize=16)
plt.xlabel("x (cm)", fontsize=14)
plt.xlim(0)
plt.ylabel("Log(Concentration B11)", fontsize=14)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend(fontsize=12)
plt.savefig("/Users/karimel-refai/classes/ee143/lab_report1/B_concentrations_subsequent.png")
# plt.show()
plt.close()
