import numpy as np

# Initial distances (mph from path segment/sensors)
velocities = np.array([55, 62, 48])
drag_factors = np.array([0.98, 0.99, 0.97])
window_size = 4  # Rolling window for smoothing
threshold = 5  # mph per frame (safe change)
mean_history = []  # Track per frame means for rolling
prev_rolling = None  # For accel calc

# Simulate 8 frames (time steps)
for frame in range(8):
    # Simulate acceleration: Add incremental mph
    accel_increment = 2 * (frame + 1)  # Grows: 2, 4, ..., 16 mph added
    current_accel = velocities + accel_increment

    # Apply drag adjustments
    adjusted = current_accel * drag_factors

    # Per frame mean velocity
    frame_mean = np.mean(adjusted)
    mean_history.append(frame_mean)

    # Rolling mean (if enough data)
    if len(mean_history) >= window_size:
        current_rolling = np.mean(mean_history[-window_size:])
        print(f"Frame {frame + 1}: Rolling velocity: {current_rolling:.1f} mph")

        # Acceleration check
        if prev_rolling is not None:
            accel = abs(current_rolling - prev_rolling)
            if accel > threshold:
                print("Unsafe Spike")
            else:
                print("Smooth-Execute Path")
        prev_rolling = current_rolling
    else:
        print(f"Frame {frame + 1}: Building...Frame mean {frame_mean:.1f} mph")

# Summary: Final smoothed velocity
final_mean = np.mean(mean_history[-window_size])
print(f"\nFinal smoothed velocity: {final_mean:.1f} mph")
