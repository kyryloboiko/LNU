import numpy as np
import matplotlib.pyplot as plt

models = ['Logistic Regression', 'Neural Network']
accuracy = [0.70, 0.70]
macro_avg = [0.35, 0.35]
weighted_avg = [0.49, 0.49]

x = np.arange(len(models))

fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(x - 0.2, accuracy, 0.4, label='Accuracy', color='blue')
ax.bar(x + 0.2, macro_avg, 0.4, label='Macro Avg', color='green')
ax.bar(x + 0.2, weighted_avg, 0.4, label='Weighted Avg', color='red')

ax.set_ylabel('Metric Value')
ax.set_title('Comparison of Accuracy and Average Metrics')
ax.set_xticks(x)
ax.set_xticklabels(models)
ax.legend()

plt.show()
