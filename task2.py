import numpy as np
from scipy.integrate import solve_ivp

M = 100
r = 0.15
TARGET = 90

def learning_rate(t, K):
    return r * (M - K)

def hit_90(t, K):
    return K[0] - TARGET
hit_90.terminal = True
hit_90.direction = 1

def time_to_90(K0):
    sol = solve_ivp(
        learning_rate,
        (0, 30),
        y0=[K0],
        events=hit_90
    )
    return None if sol.t_events[0].size == 0 else float(sol.t_events[0][0])

# Дані
K0_list = [5, 10, 20]
rows = [(K0, time_to_90(K0)) for K0 in K0_list]

# База: K(0)=5
t90_base = rows[0][1]

# Таблиця
header = "{:<8} | {:>12} | {:>24}".format("K(0), %", "t_90, днів", "Δt = t90(K0)-t90(5), дн")  # [page:0]
line = "-" * len(header)

print(header)
print(line)

for i, (K0, t90) in enumerate(rows):
    # t_90
    t90_str = "—" if t90 is None else "{:.4f}".format(t90)  # [page:0]

    # Δt: для базового рядка пусто; для інших — від’ємні значення, якщо швидше
    if i == 0 or t90 is None or t90_base is None:
        diff_str = "—"
    else:
        diff = t90 - t90_base   # буде < 0, якщо K0 досягає 90% швидше за K0=5
        diff_str = "{:.4f}".format(diff)  # [page:0]

    print("{:<8} | {:>12} | {:>24}".format(K0, t90_str, diff_str))
