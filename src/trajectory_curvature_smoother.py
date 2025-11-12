import numpy as np

# Radians, positive = left curve, negative = right curve
curvatures = np.array([0.05, -0.02, 0.08])

# Multipliers to correct lens/sensor biases
calibration_factors = np.array([1.02, 0.98, 1.01])

# Number of frames in loop
num_frames = 7

# Incremental curvature increase per frame, simulating tightening curve
curvature_inc = 0.02

# List to track per frame mean
mean_history = []

# Grab the last 4 averages in the list
window_size = 4

# Safety delta limit
curve_limit = 0.1

# For delta calculation
previous_rolling = None

# Initialize per frame loop
for frame in range(num_frames):
    cumulative_curvature_offset = curvature_inc * (frame + 1)
    current_curvatures = curvatures + cumulative_curvature_offset
    adjusted = current_curvatures * calibration_factors
    frame_mean = np.mean(adjusted)
    mean_history.append(frame_mean)

    # Rolling mean (if enough data)
    if len(mean_history) >= window_size:
        current_rolling = np.mean(mean_history[-window_size:])
        print(f"Frame {frame + 1}: Rolling mean curvature = {current_rolling:.3f} rad")

        # Check if curvature over safety limit
        if previous_rolling is not None:
            curvature_delta = abs(current_rolling - previous_rolling)
            if curvature_delta > curve_limit:
                print("Sharp curve ahead-ease steering")
            else:
                print("Smooth curve-maintain trajectory")
        previous_rolling = current_rolling
    else:
        print(f"Frame {frame + 1} Building...Frame mean = {frame_mean:.3f} rad")

# Summary: Final smoothed curvature
final_mean = np.mean(mean_history[-window_size:])
print(f"\nFinal smoothed curvature: {final_mean:.3f} rad")
