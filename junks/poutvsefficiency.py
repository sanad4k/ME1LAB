import matplotlib.pyplot as plt

# Data for Voltage Regulation (VR) Lag and Lead
vr_lag = [0.4, 0.8, 1.2, 1.59, 1.99, 2.39, 2.79, 3.19, 3.59, 3.99]
vr_lead = [-0.24, -0.48, -0.72, -0.96, -1.2, -1.44, -1.68, -1.92, -2.16, -2.4]
# Data for Power Output (Po)
pout = [25.0, 50.0, 75.0, 100.0, 125.0, 150.0, 175.0, 200.0, 225.0, 250.0]

# Round values for neatness (optional, if required)
vr_lag = [round(v, 2) for v in vr_lag]
vr_lead = [round(v, 2) for v in vr_lead]

# Plot Voltage Regulation (VR) Lag vs Power Output (Po)
plt.figure(figsize=(10, 5))
plt.plot(pout, vr_lag, marker='o', linestyle='-', color='blue', label='VR Lag')
plt.title('Voltage Regulation (Lag) vs Power Output', fontsize=14)
plt.xlabel('Power Output (Po) [W]', fontsize=12)
plt.ylabel('Voltage Regulation (VR) [%]', fontsize=12)
plt.grid(True)
plt.legend()
plt.savefig('vr_lag_vs_pout.png')  # Save the plot as an image
plt.show()

# Plot Voltage Regulation (VR) Lead vs Power Output (Po)
plt.figure(figsize=(10, 5))
plt.plot(pout, vr_lead, marker='o', linestyle='-', color='red', label='VR Lead')
plt.title('Voltage Regulation (Lead) vs Power Output', fontsize=14)
plt.xlabel('Power Output (Po) [W]', fontsize=12)
plt.ylabel('Voltage Regulation (VR) [%]', fontsize=12)
plt.grid(True)
plt.legend()
plt.savefig('vr_lead_vs_pout.png')  # Save the plot as an image
plt.show()
