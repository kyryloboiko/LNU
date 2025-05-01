import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def load_data(file_path):
    data = np.loadtxt(file_path, delimiter="\t", skiprows=1,
                      dtype={'names': ('RANK', 'NGramm', 'F'), 'formats': (np.int32, 'U10', np.int32)})
    return data['RANK'], data['F']


# Експоненційна функція для закону Гіпса
def gibbs_func(rank, a, b):
    return a * np.exp(-b * rank)


# Функція для побудови графіку
def plot_log_scale(rank, freq, title, xlabel, ylabel):
    # Логарифмічне перетворення
    log_rank = np.log10(rank)
    log_freq = np.log10(freq)

    # Лінійна апроксимація
    slope, intercept = np.polyfit(log_rank, log_freq, 1)

    # Побудова графіку
    plt.figure(figsize=(8, 6))
    plt.scatter(log_rank, log_freq, label="Дані", color='blue')
    plt.plot(log_rank, slope * log_rank + intercept, label=f"Лінія апроксимації\nY = {slope:.2f}X + {intercept:.2f}",
             color='red')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.show()

    print(f"Результати для {title}:")
    print(f"  Кут нахилу (slope): {slope}")
    print(f"  Вільний член (intercept): {intercept}")
    print("-" * 50)


# Графік для закону Гіпса
def plot_gibbs(rank, freq):
    # Підбір параметрів a та b
    popt, _ = curve_fit(gibbs_func, rank, freq, p0=(freq[0], 0.01))

    print(f"Параметри закону Гіпса: a = {popt[0]:.3f}, b = {popt[1]:.3f}")

    # Побудова графіка
    plt.figure(figsize=(8, 6))
    plt.scatter(rank, freq, label="Дані", color='blue', alpha=0.6)
    plt.plot(rank, gibbs_func(rank, *popt), label=f"Апроксимація: f(r) = {popt[0]:.3f} * exp(-{popt[1]:.3f} * r)",
             color='red', linewidth=2)

    plt.title("Закон Гіпса")
    plt.xlabel("Rank")
    plt.ylabel("Frequency")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.show()


def main():
    file_path = "TextShuffler_n-grams.txt"
    rank, freq = load_data(file_path)

    # Побудова графіків для законів
    plot_log_scale(rank, freq, "Перший закон Ціпфа", "log(Rank)", "log(Frequency)")
    plot_log_scale(freq, rank, "Другий закон Ціпфа", "log(Frequency)", "log(Rank)")

    # Для закону Парето
    cumulative_freq = np.cumsum(freq[::-1])[::-1]
    plot_log_scale(freq, cumulative_freq, "Закон Парето", "log(Frequency)", "log(Cumulative Frequency)")

    # Для закону Гіпса
    plot_gibbs(rank, freq)


if __name__ == "__main__":
    main()
