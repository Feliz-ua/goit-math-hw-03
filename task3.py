import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

#Визначемо функцію інтенсивності 
def f(t):
    return 500* np.exp(-0.3*t)

# Обчислимо інтеграл від 0 до 7
numerical_result, _ = quad(f, 0, 7)
print(f"Чисельне значення інтегралу від 0 до 7: {numerical_result:.2f}")

# Діапазон часу (від 0 до 30 днів)
t_values = np.linspace(0, 30, 500)
f_values = f(t_values)

# Діапазон для першого тиждня (від 0 до 7 днів)
t_week1 = np.linspace(0, 7, 50)
f_week1 = f(t_week1)

plt.figure(figsize=(10, 6))
plt.plot(t_values, f_values, label='Інтенсивність реєстрацій на новий онлайн-курс ($f(t)=500*e^{-0.3t}$)', color='blue', linewidth=2)

# Заповнення під кривою для першого тижня
plt.fill_between(t_week1, f_week1, color='orange', alpha=0.5, label='Реєстрації користувачів за 1-й тиждень')
plt.title('Динаміка інтенсивності реєстрацій користувачів')
plt.xlabel('Час (дні)')
plt.ylabel('Інтенсивність реєстрацій')
plt.legend()
plt.grid(True)
plt.show()