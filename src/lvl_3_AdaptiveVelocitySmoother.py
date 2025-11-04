import numpy as np

# Initial velocities
velocities = np.array([55, 62, 48])

# Drag facors array
drag_factors = np.array([0.98, 0.99, 0.97])

noise_std = 2.0
num_frames = 6
window_size = 3
accel_limit = 4.0
mean_history = []
previous_rolling = None

for frame in range(num_frames):
    accel_increment = 1 * (frame + 1)
    current_accel = velocities + accel_increment
    adjusted = current_accel * drag_factors
    noise = np.random.normal(0, noise_std, size=len(velocities))
    noise_adj = adjusted + noise
    frame_mean = np.mean(noise_adj)
    mean_history.append(frame_mean)

    if len(mean_history) >= window_size:
        current_rolling = np.mean(mean_history[-window_size:])
        print(f"Frame {frame + 1}: Rolling velocity: {current_rolling:.1f} mph")

        if previous_rolling is not None:
            accel = abs(current_rolling - previous_rolling)
            if accel > accel_limit:
                print("Alert: Big jump-slow down!")
            else:
                print("Smooth-keep going")
        previous_rolling = current_rolling
    else:
        print(f"Frame {frame + 1}: Building window... Frame mean = {frame_mean:.1f} mph")

# Final Summary
final_rolling = np.mean(mean_history[-window_size:])
print(f"Final mean vel = {final_rolling:.1f} mph")
