from scipy.integrate import quad
import numpy as np

f1 = lambda x: 3 * np.sqrt(x)
result1, _ = quad(f1, 4, 9)
print(f"(a) ∫₄⁹ 3√x dx = {result1:.2f}")

