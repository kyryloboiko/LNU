import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

# Задати кількість істинних та хибних позитивних/негативних для кожної моделі
# Матриця плутанини: [[TN, FP], [FN, TP]]

# Логістична регресія
cm_logreg = [[7048, 0], [3021, 0]]

# Нейронна мережа (10 поколінь)
cm_nn_10 = [[7048, 0], [3021, 0]]

# Нейронна мережа (110 поколінь)
cm_nn_110 = [[7048, 0], [3021, 0]]

# Нейронна мережа (1110 поколінь)
cm_nn_1110 = [[7048, 0], [3021, 0]]

# Створення підграфіків для кожної моделі
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Логістична регресія
sns.heatmap(cm_logreg, annot=True, fmt='d', cmap='Blues', ax=axes[0, 0], cbar=False)
axes[0, 0].set_title('Confusion Matrix - Logistic Regression')
axes[0, 0].set_xlabel('Predicted')
axes[0, 0].set_ylabel('True')

# Нейронна мережа (10 поколінь)
sns.heatmap(cm_nn_10, annot=True, fmt='d', cmap='Blues', ax=axes[0, 1], cbar=False)
axes[0, 1].set_title('Confusion Matrix - Neural Network (10 epochs)')
axes[0, 1].set_xlabel('Predicted')
axes[0, 1].set_ylabel('True')

# Нейронна мережа (110 поколінь)
sns.heatmap(cm_nn_110, annot=True, fmt='d', cmap='Blues', ax=axes[1, 0], cbar=False)
axes[1, 0].set_title('Confusion Matrix - Neural Network (110 epochs)')
axes[1, 0].set_xlabel('Predicted')
axes[1, 0].set_ylabel('True')

# Нейронна мережа (1110 поколінь)
sns.heatmap(cm_nn_1110, annot=True, fmt='d', cmap='Blues', ax=axes[1, 1], cbar=False)
axes[1, 1].set_title('Confusion Matrix - Neural Network (1110 epochs)')
axes[1, 1].set_xlabel('Predicted')
axes[1, 1].set_ylabel('True')

plt.tight_layout()
plt.show()
