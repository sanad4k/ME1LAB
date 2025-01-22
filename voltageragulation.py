import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
mode = ['lag', 'lead']

# Constants
Isc = 5.68  # Short circuit current
R02 = 1.5389  # Resistance
Xo2 = 1.262  # Reactance
v2 = 220  # Per-unit voltage (can be adjusted if needed)
load_values = [i / 10 for i in range(1, 11)]  # Load values (x): 0.1 to 1.0
power_factors = [0.2, 0.4, 0.6, 0.8, 1.0]  # Power factors (pf)

# Function to calculate phi from power factor
def calculate_phi(pf):
    return np.arccos(pf)  # Return phi in radians

# Function to calculate voltage regulation
def calculate_voltage_regulation(x, pf):
    phi = calculate_phi(pf)
    for m in mode:
        if m == 'lag':
            vrlead = x * (Isc / v2) * (R02 * np.cos(phi) - Xo2 * np.sin(phi)) * 100
        else:
            vrlag = x * (Isc / v2) * (R02 * np.cos(phi) + Xo2 * np.sin(phi)) * 100


    return vrlag , vrlead

# Create a list to store results
results = []

# Perform calculations for each combination of load and power factor
for pf in power_factors:
    for x in load_values:
        vrlag ,vrlead  = calculate_voltage_regulation(x, pf)
        results.append({
            "Load (x)": x,
            "Power Factor (pf)": pf,
            "Voltage Regulation (%) (lag)": round(vrlag, 2),
            "Voltage Regulation (%) (lead)": round(vrlead, 2)
        })

i = 0
for x in load_values:
    print(results[i]["Voltage Regulation (%) (lag)"])
    i+=1
print("------------------------------------------------------ ")
i = 0
for x in load_values:
    print(results[i]["Voltage Regulation (%) (lead)"])
    i+=1

# Convert results to a DataFrame for a structured table
df = pd.DataFrame(results)

# Save the table to a CSV file
df.to_csv("voltage_regulation_results.csv", index=False)
print("Results saved to 'voltage_regulation_results.csv'")

# Plot voltage regulation vs load for each power factor
plt.figure(figsize=(10, 6))
for pf in power_factors:
    subset = df[df["Power Factor (pf)"] == pf]
    plt.plot(subset["Power Factor (pf)"], subset["Voltage Regulation (%) (lag)"], label=f"PF = {pf} , mode = lag")
    plt.plot(subset["Power Factor (pf)"], subset["Voltage Regulation (%) (lead)"], label=f"PF = {pf} , mode = lead")

# Add labels, legend, and title
plt.title("Voltage Regulation vs pf", fontsize=16)
plt.xlabel("Load (x)", fontsize=14)
plt.ylabel("Voltage Regulation (%)", fontsize=14)
plt.legend(title="Power Factor", fontsize=12)
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()

# Optionally save the plot as an image
plt.savefig("voltage_regulation_plot.png")
print("Plot saved as 'voltage_regulation_plot.png'")
