import numpy as np

speeds = np.array([60, 70, 80])
adjustments = np.array([0.9, 1.0, 0.95])
adjusted = speeds * adjustments
min_speed = np.min(adjusted)
print(f"Optimized min speed: {min_speed} mph")
