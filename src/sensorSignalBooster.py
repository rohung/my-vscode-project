import numpy as np

signals = np.array([45, 62, 38])
boosts = np.array([1.2, 1.1, 1.3])
boosted = signals * boosts
max_signal = np.max(boosted)
print(f"Strongest signal: {max_signal:.1f}")
