import numpy as np
import scipy.integrate as spi

def f(x):
    return x ** 2

a, b = 0, 2
N = 1_000_000
np.random.seed(42)

#Метод Монте-Карло
x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(0, f(b), N)
under_curve = y_rand <= f(x_rand)

area_rect = (b - a) * f(b)
mc_integral = area_rect * np.sum(under_curve) / N

#Перевірка через quad
quad_result, quad_error = spi.quad(f, a, b)

#Аналітичний результат
analytical = 8 / 3

#Порівняння
print(f"Монте-Карло (N=1M): {mc_integral:.6f}")
print(f"scipy quad:         {quad_result:.6f}  (похибка: {quad_error:.2e})")
print(f"Аналітичний (8/3):  {analytical:.6f}")
print(f"Відхилення MC:      {abs(mc_integral - analytical) / analytical * 100:.4f}%")