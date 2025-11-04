import numpy as np

levels = np.array([85, 78, 92])
drains = np.array([0.05, 0.08, 0.02])

steps = 0
max_steps = 5
current_levels = levels.copy()
critical_step = None

while steps < max_steps:
    drain_amount = current_levels * drains
    current_levels = current_levels - drain_amount
    min_level = np.min(current_levels)

    if min_level < 20:
        critical_step = steps + 1
        break
    steps += 1

print(f"Survived {steps} steps. Final min level: {min_level:.1f}%")
if critical_step:
    print(f"Critical hit at step {critical_step}!")
else:
    print("Survived all steps!")
