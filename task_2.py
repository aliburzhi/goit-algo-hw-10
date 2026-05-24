import numpy as np

def f(x):
    return x ** 2

a, b = 0, 2
N = 1_000_000
np.random.seed(42)

x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(0, f(b), N)
under_curve = y_rand <= f(x_rand)
area_rect = (b - a) * f(b)
mc_integral = area_rect * np.sum(under_curve) / N