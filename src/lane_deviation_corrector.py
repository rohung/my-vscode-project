import numpy as np

# Initial deviations (meters from lane center; + = right drift)
deviations = np.array([0.2, -0.1, 0.3])

# Correction factors (multipliers to adjust drift)
correction_factors = np.array([0.95, 1.02, 0.98])

# Simulation parameters
drift_inc = 0.05
num_frames = 6
window_size = 3
safe_drift = 0.5

# Tracking
mean_history = []

# Simulate 6 frames
for frame in range(num_frames):

    # Add drift for this frame
    cumulative_drift = drift_inc * (frame + 1)
    
    # Apply deviations to drift
    current_devs = deviations + cumulative_drift
    
    # Apply corrections
    adjusted = current_devs * correction_factors
    
    # Per frame mean deviation
    frame_mean = np.mean(adjusted)
    mean_history.append(frame_mean)

    # Check if list has 3 or more data
    if len(mean_history) >= window_size:
        rolling_mean = np.mean(mean_history[-window_size:])
        print(f"Frame {frame + 1}: Rolling mean deviation = {rolling_mean:.2f} m")
        
        if abs(rolling_mean) > safe_drift:
            print("Drift detected-correct steering!")
        else:
            print("Stable in lane")
    else:
        print(f"Frame: {frame + 1} Building...Frame mean = {frame_mean:.2f} m")

# Summary : Final smoothed deviation
final_mean = np.mean(mean_history[-window_size:])
print(f"\nFinal smoothed deviation: {final_mean:.2f} m")