import numpy as np
import matplotlib.pyplot as plt


file_path = "1.txt"
fixed_file_path = "1_fix.txt"

with open(file_path, 'r', encoding='utf-8') as infile, open(fixed_file_path, 'w', encoding='utf-8') as outfile:
    for line in infile:
        outfile.write(line.replace(',', '.'))

data_fixed = np.loadtxt(fixed_file_path, delimiter='\t', skiprows=1)

L = data_fixed[:, 0]  # Довжина
V = data_fixed[:, 1]  # Об'єм
dV = data_fixed[:, 2]  # Різниця об'ємів

# Логарифмічні перетворення
log_L = np.log(L)
log_V = np.log(V)

# Лінійна апроксимація залежності V(L) ∝ L^p
coeffs = np.polyfit(log_L, log_V, 1)
p = coeffs[0]  # Коефіцієнт нахилу
intercept = coeffs[1]

plt.figure(figsize=(10, 6))
plt.scatter(log_L, log_V, color='green', label='Дані (логарифмічні координати)')
plt.plot(log_L, np.polyval(coeffs, log_L), color='orange', label=f"Апроксимація: p ≈ {p:.2f}")

plt.title("Лінійна апроксимація для закону Гіпса")
plt.xlabel("log(L)")
plt.ylabel("log(V)")
plt.legend()
plt.grid(True)

plt.show()

print(f"Коефіцієнт нахилу (p): {p:.2f}")
print(f"Перетин з віссю (intercept): {intercept:.2f}")
