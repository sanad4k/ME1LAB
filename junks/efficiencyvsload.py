import matplotlib.pyplot as plt

# Data for Load and Efficiency
load = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
efficiency = [
    78.36990595611285, 85.61643835616438, 87.31082654249126,
    87.4125874125874, 86.86587908269632, 86.0091743119266,
    84.99271491015055, 83.89261744966443, 82.75101140125047,
    81.59268929503916
]

# Plotting Efficiency vs Load
plt.figure(figsize=(10, 5))
plt.plot(load, efficiency, marker='o', linestyle='-', color='b', label="Efficiency")
plt.title('Efficiency vs Load')
plt.xlabel('Load (x)')
plt.ylabel('Efficiency (%)')
plt.grid(True)
plt.legend()
plt.tight_layout()

# Show plot
plt.savefig("efficiency_vs_load.png")  # Saves the plot as a PNG file
plt.show()
