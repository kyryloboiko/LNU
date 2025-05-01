import numpy as np
import matplotlib.pyplot as plt


def fix_file_format(file_path, fixed_file_path):
    with open(file_path, 'r', encoding='utf-8') as infile, open(fixed_file_path, 'w', encoding='utf-8') as outfile:
        for line in infile:
            outfile.write(line.replace(',', '.'))


def process_and_plot(data, x_label, y_label, title, color_data, color_fit, law_name):
    # Розділення даних
    x = data[:, 0]
    y = data[:, 1]

    # Логарифмічні перетворення
    log_x = np.log(x)
    log_y = np.log(y)

    # Лінійна апроксимація
    coeffs = np.polyfit(log_x, log_y, 1)
    slope = -coeffs[0]
    intercept = coeffs[1]

    # Виведення результатів
    print(f"{law_name}:")
    print(f"Коефіцієнт нахилу (β/α): {slope:.2f}")
    print(f"Перетин з віссю (інтерцепт): {intercept:.2f}")
    print("-" * 50)

    plt.figure(figsize=(10, 6))
    plt.scatter(log_x, log_y, color=color_data, label='Дані (логарифмічні координати)')
    plt.plot(log_x, np.polyval(coeffs, log_x), color=color_fit, label=f"Апроксимація: β/α ≈ {slope:.2f}")

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.grid(True)
    plt.show()

# Закон Зіпфа
file_path_zipf2 = 'data2/zipf2_plot_data.txt'
fixed_file_path_zipf2 = 'data/zipf2_plot_data_fixed.txt'
fix_file_format(file_path_zipf2, fixed_file_path_zipf2)
data_zipf2 = np.loadtxt(fixed_file_path_zipf2, delimiter='\t', skiprows=1)
process_and_plot(
    data_zipf2,
    "log(F)", "log(PDF)",
    "Лінійна апроксимація для першого та другого закону Зіпфа",
    color_data="purple", color_fit="orange",
    law_name="Перший та другий закон Зіпфа"
)

# Закон Парето
file_path_pareto = 'data2/pareto_plot_data.txt'
fixed_file_path_pareto = 'data/pareto_plot_data_fixed.txt'
fix_file_format(file_path_pareto, fixed_file_path_pareto)
data_pareto = np.loadtxt(fixed_file_path_pareto, delimiter='\t', skiprows=1)
process_and_plot(
    data_pareto,
    "log(x)", "log(y)",
    "Лінійна апроксимація для закону Парето",
    color_data="green", color_fit="orange",
    law_name="Закон Парето"
)