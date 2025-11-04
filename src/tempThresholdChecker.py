import numpy as np

temps = np.array([210, 195, 220])
cools = np.array([0.95, 0.98, 0.92])
tweaked = temps * cools
avg_temp = np.mean(tweaked)
print(f"Average safe temp:{avg_temp:.1f}F")
