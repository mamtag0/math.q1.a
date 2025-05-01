from scipy.integrate import quad
import numpy as np

f3 = lambda x: np.arccos(x)
result3, _ = quad(f3, 0, 1)
print(f"(c) ∫₀¹ arccos(x) dx = {result3:.2f}")
