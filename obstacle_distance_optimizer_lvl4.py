import numpy as np

# initial distances of 3 obstacles
distances = np.array([120, 80, 150])
error_factors = np.array([1.05, 0.95, 1.10])
window_size = 3  # For rolling min
approach_rate = 10  # ft per frame (obstacle closing in)
safe_rolling_min = 60  # Alert threshold
min_history = []  # Track per frame mins for rolling

# Loop through 5 frames
for frame in range(5):
    # Simulate approach: Subtract rate from all distances
    current_distances = distances - (approach_rate * (frame + 1))

    # Apply error adjustments
    adjusted = current_distances * error_factors

    # Per-frame min
    frame_min = np.min(adjusted)
    min_history.append(frame_min)

    # Rolling min check (if enough data)
    if len(min_history) >= window_size:
        rolling_min = np.min(min_history[-window_size:])
        print(f"Frame {frame + 1} Rolling min = {rolling_min:.1f} ft")

        if rolling_min < safe_rolling_min:
            print("Approaching threat-decelerate!")
        else:
            print("Stable-maintain speed.")
    else:
        print(f"Frame {frame + 1}: Building...Frame min = {frame_min:.1f} ft")

# Summary: Overall closest
overall_min = np.min(min_history)
print(f"\nOverall closest: {overall_min:.1f} ft")
