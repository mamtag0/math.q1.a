from scipy.integrate import quad
import numpy as np

f2 = lambda x: np.log(x)
result2, _ = quad(f2, 1, np.e)
print(f"(b) ∫₁ᵉ ln(x) dx = {result2:.2f}")
