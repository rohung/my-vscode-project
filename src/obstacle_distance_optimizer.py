import numpy as np

# Raw distances to obstacles (feet)
distances = np.array([120, 80, 150])

# Error factors (multipliers for sensor inaccuracy)
error_factors = np.array([1.05, 0.95, 1.10])

# Apply adjustments (vectorized)
adjusted = distances * error_factors

# Find the closest threat
min_adjusted = np.min(adjusted)

# Decision
safe_threshold = 50.0
if min_adjusted < safe_threshold:
    print(f"Closest obstacle: {min_adjusted:.1f} Brake immediately!")
else:
    print(f"Closest obstacle {min_adjusted:.1f} Safe to proceed")
