import numpy as np
from scipy.optimize import approx_fprime

# 1. Визначення функцій
def f_load(x):
    """
    Функція навантаження f(t).
    approx_fprime очікує масив, тому беремо t = x[0]
    """
    t = x[0]
    return 1000 * t * np.exp(-0.2 * t)

def f_derivative_analytical(t):
    """Аналітична формула похідної f'(t), виведена нами."""
    return 1000 * np.exp(-0.2 * t) * (1 - 0.2 * t)

# 2. Параметри для аналізу
time_points = [2, 6, 10]  # t=2 (10:00), t=6 (14:00), t=10 (18:00)
epsilon = np.sqrt(np.finfo(float).eps) # Оптимальний крок для чисельного методу

print(f"{'Час (t)':<10} {'Година':<10} {'Чисельна f\'(t)':<20} {'Аналітична f\'(t)':<20} {'Різниця'}")
print("-" * 75)

# 3. Обчислення та виведення
for t in time_points:
    # Чисельне диференціювання
    # approx_fprime повертає масив градієнтів, беремо [0]
    f_prime_num = approx_fprime(np.array([t]), f_load, epsilon)[0]
    
    # Аналітичне обчислення
    f_prime_ana = f_derivative_analytical(t)
    
    # Форматування часу
    clock_time = f"{8+t}:00"
    
    # Різниця
    diff = abs(f_prime_num - f_prime_ana)
    
    print(f"{t:<10} {clock_time:<10} {f_prime_num:<20.4f} {f_prime_ana:<20.4f} {diff:.2e}")