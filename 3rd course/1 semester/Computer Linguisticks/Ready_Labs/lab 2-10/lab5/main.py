import numpy as np
import matplotlib.pyplot as plt


def fix_file_format(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as infile, open(output_path, 'w', encoding='utf-8') as outfile:
        for line in infile:
            outfile.write(line.replace(',', '.'))

def calculate_gibbs_law(L, V, method="equal_bins", num_bins=32):
    if method == "equal_bins":
        bins = np.linspace(np.min(L), np.max(L), num_bins + 1)
    elif method == "equal_points":
        step = len(L) // num_bins
        if step == 0:
            raise ValueError("Кількість точок у масиві L менша за num_bins")
        indices = list(range(0, len(L), step)) + [len(L) - 1]
        bins = [L[i] for i in indices]
    elif method == "exponential_bins":
        bins = np.logspace(np.log10(np.min(L)), np.log10(np.max(L)), num_bins + 1)
    else:
        raise ValueError("Unknown binning method")

    bin_centers = []
    bin_means = []
    for i in range(len(bins) - 1):
        mask = (L >= bins[i]) & (L < bins[i + 1])
        if np.sum(mask) > 0:
            bin_centers.append((bins[i] + bins[i + 1]) / 2)
            bin_means.append(np.mean(V[mask]))

    return np.array(bin_centers), np.array(bin_means)


def plot_graph(L, V, method, num_bins):
    centers, means = calculate_gibbs_law(L, V, method, num_bins)

    # Логарифмічні перетворення
    log_centers = np.log(centers)
    log_means = np.log(means)

    # Лінійна апроксимація
    coeffs = np.polyfit(log_centers, log_means, 1)
    slope = coeffs[0]
    intercept = coeffs[1]

    plt.figure(figsize=(10, 6))
    plt.scatter(log_centers, log_means, color='black', label='Дані (логарифмічні координати)')
    plt.plot(log_centers, np.polyval(coeffs, log_centers), color='red', label=f"Апроксимація: θ ≈ {slope:.2f}")
    plt.title(f"Закон Гіпса ({method})")
    plt.xlabel("log(L)")
    plt.ylabel("log(V)")
    plt.legend()
    plt.grid(True)
    plt.show()

    return slope

original_file_path = "2.1.txt"
fixed_file_path = "2.1fix.txt"
fix_file_format(original_file_path, fixed_file_path)

data = np.loadtxt(fixed_file_path, delimiter='\t', skiprows=1)

L = data[:, 0]
V = data[:, 1]

methods = ["equal_bins", "equal_points", "exponential_bins"]
num_bins = 20

results = {}
for method in methods:
    slope = plot_graph(L, V, method, num_bins)
    results[method] = slope

print("Результати дослідження:")
for method, slope in results.items():
    print(f"Метод {method}: θ ≈ {slope:.2f}")
