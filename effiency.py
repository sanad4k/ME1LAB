import pandas as pd
import matplotlib.pyplot as plt

# Input constants
s = 1250  # Apparent power
pcu = 50  # Copper losses
piron = 6.4  # Iron losses
load_values = [i / 10 for i in range(1, 11)]  # Load values (x): 0.1 to 1.0
power_factors = [0.2, 0.4, 0.6, 0.8, 1.0]  # Power factors (pf)

# Function to calculate power output
def calculate_power_output(x, pf):
    return x * s * pf

# Function to calculate efficiency
def calculate_efficiency(po, x):
    total_loss = (x ** 2) * pcu + piron
    return po / (po + total_loss)

# Create a list to store results
results = []

# Perform calculations for each combination of load and power factor
for pf in power_factors:
    for x in load_values:
        po = calculate_power_output(x, pf)
        efficiency = calculate_efficiency(po, x)
        results.append({
            "Load (x)": x,
            "Power Factor (pf)": pf,
            "Power Output (Po)": po,
            "Efficiency (%)": efficiency * 100
        })

i = 0
for x in load_values:
    print(results[i]["Efficiency (%)"]) 
    i+=1
i = 0
print("------------------------------------------------------ ")
for x in load_values:
    print(results[i]["Load (x)"]) 
    i+=1
# print(results)

# Convert results to a DataFrame for a structured table
df = pd.DataFrame(results)

# Plot efficiency vs power output for each power factor
plt.figure(figsize=(10, 6))
for pf in power_factors:
    subset = df[df["Power Factor (pf)"] == pf]
    plt.plot(subset["Power Output (Po)"], subset["Efficiency (%)"], label=f"PF = {pf}")

# Add labels, legend, and title
plt.title("Efficiency vs Power Output", fontsize=16)
plt.xlabel("Power Output (Po)", fontsize=14)
plt.ylabel("Efficiency (%)", fontsize=14)
plt.legend(title="Power Factor", fontsize=12)
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()

# Optionally save the plot as an image
plt.savefig("efficiency_vs_power_output.png")
print("\nPlot saved as 'efficiency_vs_power_output.png'")
