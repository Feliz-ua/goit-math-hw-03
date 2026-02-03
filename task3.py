import numpy as np
from scipy.integrate import quad

#Визначемо функцію інтенсивності 
def f(t):
    return 500* np.exp(-0.3*t)

# Обчислимо інтеграл від 0 до 7
numerical_result, _ = quad(f, 0, 7)
print(f"Чисельне значення інтегралу від 0 до 7: {numerical_result:.2f}")
