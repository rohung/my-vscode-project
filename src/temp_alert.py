import numpy as np
import matplotlib.pyplot as plt

temps = np.array([210, 195, 220])
cools = np.array([0.95, 0.98, 0.92])
threshold = 200
window_size = 3
temp_list = []
temp_plot = []
alerts = []

# Simulate 10 time steps
for step in range(10):

    # Add random noise (+-5F) to simulate flutuations
    noise = np.random.normal(loc=0, scale=5, size=len(temps))
    new_temps = temps + noise

    # Apply cooling factors
    cooled_temps = new_temps * cools

    # Compute per-step average (mean across sensors)
    avg_cooled = np.mean(cooled_temps)
    temp_list.append(avg_cooled)
    temp_plot.append(cooled_temps.copy())  # Store full array for plot

    # Rolling average check (last 3 steps, if available)
    if len(temp_list) >= window_size:
        rolling_avgs = np.mean(temp_list[-window_size])
        print(f"Step {step + 1}: Rolling avg = {rolling_avgs:.1f}F")

        if rolling_avgs > threshold:
            alert_message = f"Warning: Temp over threshold at step #{step + 1}"
            print(alert_message)
            alerts.append(step + 1)

    else:
        print(f"Step{step + 1}:building window...Step avg = {avg_cooled:.1f}F")

# Summary output
final_avg = np.mean(temp_list)
num_alerts = len(alerts)
print(f"Final avg = {final_avg:.1f}F, alerts = {num_alerts}")
if alerts:
    print(f"Alert steps: {alerts}")

# Plot: Temps over time (mean per step, with rolling avg line)
steps = np.arange(1, len(temp_list) + 1)
plt.figure(figsize=(10, 6))
plt.plot(steps, temp_list, label='Step Avg Temp', marker='o')

# Rolling avg line (compute for plot)
rolling_avgs = []
for i in range(len(temp_list)):
    if i >= window_size - 1:
        rolling_avgs.append(np.mean(temp_list[i - window_size + 1:i +1]))
    else:
        rolling_avgs.append(temp_list[i])

plt.plot(steps, rolling_avgs, label='Rolling 3-Step Avg', linestyle='--', marker='s')
plt.axhline(y=threshold, color='r', linestyle=':', label='Threshold (200°F)')
plt.xlabel('Time Steps')
plt.ylabel('Temperature (°F)')
plt.title('Temperature Trends Over Time')
plt.legend()
plt.grid(True)
plt.show()
