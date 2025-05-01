import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress


def analyze_ngrams(file_path, ngram_label):
    data = pd.read_csv(file_path, sep='\\t', header=None, names=['Ранг', 'NGram', 'Частота'], engine='python')

    data['Ранг'] = pd.to_numeric(data['Ранг'], errors='coerce')
    data['Частота'] = pd.to_numeric(data['Частота'], errors='coerce')

    data = data.dropna()

    ranks = data['Ранг']
    frequencies = data['Частота']

    # --- Звичайний масштаб ---
    plt.figure(figsize=(8, 6))
    plt.plot(ranks, frequencies, 'o-', label='Дані')
    plt.title(f'Рангово-частотна залежність для {ngram_label} (звичайний масштаб)')
    plt.xlabel('Ранг')
    plt.ylabel('Частота')
    plt.grid()
    plt.legend()
    plt.show()

    # --- Напівлогарифмічний масштаб ---
    plt.figure(figsize=(8, 6))
    plt.semilogy(ranks, frequencies, 'o-', label='Дані')
    plt.title(f'Рангово-частотна залежність для {ngram_label} (напівлогарифмічний масштаб)')
    plt.xlabel('Ранг')
    plt.ylabel('Частота (логарифмічний масштаб)')
    plt.grid()
    plt.legend()
    plt.show()

    # --- Логарифмічний масштаб ---
    log_ranks = np.log10(ranks)
    log_freqs = np.log10(frequencies)

    # Лінійна апроксимація
    slope, intercept, r_value, _, _ = linregress(log_ranks, log_freqs)
    approx_line = slope * log_ranks + intercept

    plt.figure(figsize=(8, 6))
    plt.plot(log_ranks, log_freqs, 'o', label='Дані (логарифмічний масштаб)')
    plt.plot(log_ranks, approx_line, 'r-', label=f'Апроксимація: y={slope:.2f}x+{intercept:.2f}')
    plt.title(f'Рангово-частотна залежність для {ngram_label} (логарифмічний масштаб)')
    plt.xlabel('log10(Ранг)')
    plt.ylabel('log10(Частота)')
    plt.grid()
    plt.legend()
    plt.show()

    pearson_log = r_value
    _, _, r_value_semilog, _, _ = linregress(ranks, np.log(frequencies))

    return {
        'n-грам': ngram_label,
        'Коефіцієнт нахилу': round(slope, 2),
        'Коефіцієнт Пірсона (логарифмічний)': round(pearson_log, 2),
        'Коефіцієнт Пірсона (напівлогарифмічний)': round(r_value_semilog, 2)
    }

files = [
    'data/1-grams.txt',
    'data/2-grams.txt',
    'data/3-grams.txt',
    'data/4-grams.txt'
]

results = []

for i, file_path in enumerate(files, start=1):
    ngram_label = f'{i}-грам'
    print(f'Аналізую {ngram_label}...')
    result = analyze_ngrams(file_path, ngram_label)
    results.append(result)

df_results = pd.DataFrame(results)

print("\nТаблиця результатів:")
print(df_results.to_markdown(index=False, tablefmt="grid"))
