import numpy as np

# Initial velocities
velocities = np.array([55, 62, 48])

# Drag facors array
drag_factors = np.array([0.98, 0.99, 0.97])

# Noise Parameters
noise_std = 3.0  # Standard deviation for noise (mph)

# Simulation parameters
num_frames = 10
accel_base = 1.5  # Base mph increment per frame
window_size = 4  # Rolling Window
accel_limit = 4.0  # Safe accel delta (mph/frame)
variance_limit = 2.5  # High variance threshold (mph std dev)

# Tracking Structures
mean_history = []
adjusted_history = []
alerts = []

# Helper function for velocity adjustments
def adjust_velocities(vels, increment, drag_f, noise_std):
    current = vels + increment
    dragged = current * drag_f
    noise = np.random.normal(0, noise_std, size=len(vels))
    adjusted = dragged + noise
    return adjusted

# Helper function for rolling calculations
def rolling_calcs(history, win_size):
    if len(history) < win_size:
        #  Early frames: Use full history
        return np.mean(history), np.std(history)
    else:
        #  Last window
        window = history[-win_size:]
        return np.mean(window), np.std(window)

# Helper function for tiered alerts
def tiered_alerts(accel_delta, variance, accel_lim, var_lim):
    risk = 0
    if accel_delta > accel_lim and variance > var_lim:
        message = "Emergency reroute! High accel + variance."
        risk = 3
    elif accel_delta > accel_lim or variance > var_lim:
        message = "Minor jitter-adjust path."
        risk = 2
    else:
        message = "Stable-proceed."
        risk = 1
    return message, risk

#  Main simulation loop
previous_rolling_mean = None
previous_variance = None

for frame in range(num_frames):
    # Calculate increment for this frame
    increment = accel_base * (frame + 1)

    # Adjust velocities (call helper)
    adjusted_vels = adjust_velocities(velocities, increment, drag_factors, noise_std)

    # Store full adjusted for variance history
    adjusted_history.append(adjusted_vels.copy())

    # Per-frame mean
    frame_mean = np.mean(adjusted_vels)
    mean_history.append(frame_mean)

    # Rolling calcs (call helper)
    current_mean, current_var = rolling_calcs(mean_history, window_size)

    print(f"Frame {frame + 1}: Rolling mean = {current_mean:.1f} mph, Var = {current_var:.1f} mph")

    # Acceleration and alert check (if enough history)
    if len(mean_history) >= window_size and previous_rolling_mean is not None:
        accel_delta = abs(current_mean - previous_rolling_mean)
        var_delta = abs(current_var - previous_variance) if previous_variance is not None else 0

        # Tiered alert (call helper)
        message, risk = tiered_alerts(accel_delta, current_var, accel_limit, variance_limit)
        print(f"  {message} (Risk: {risk})")
        alerts.append((frame + 1, message))
        
        previous_variance = current_var
    
    previous_rolling_mean = current_mean
    
    if len(mean_history) < window_size:
        print(f"  Building window... Frame mean = {frame_mean:.1f} mph")

# Step 10: Summary (outside loop)
final_mean = np.mean(mean_history[-window_size:])
final_var = np.std(mean_history[-window_size:])
num_alerts = len([a for a in alerts if "reroute" in a[1] or "jitter" in a[1]])
print(f"\nSummary: Final mean vel = {final_mean:.1f} mph, Avg variance = {np.mean([np.std(h) for h in adjusted_history[-window_size:]]):.1f} mph")
print(f"Total alerts: {len(alerts)}, High-risk: {num_alerts}")
if alerts:
    print("Alert details:", alerts)