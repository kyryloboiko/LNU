import re
import matplotlib.pyplot as plt
import os

file_path = "training_log.txt"

# Перевірка, чи існує файл
if not os.path.exists(file_path):
    print(f"❌ Файл не знайдено за шляхом: {file_path}")
else:
    print(f"Файл знайдено: {file_path}")

with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()
    print(f"Кількість рядків у файлі: {len(lines)}")
    print(f"Перші 5 рядків: {lines[:5]}")

# Регулярний вираз для парсингу епохи
epoch_pattern = re.compile(r"Epoch (\d+)/\d+")

# Регулярний вираз для метрик
metrics_pattern = re.compile(
    r"loss:\s*([\d.]+)\s*- accuracy:\s*([\d.]+)\s*- val_loss:\s*([\d.]+)\s*- val_accuracy:\s*([\d.]+)"
)

# Дані для графіків
epochs = []
loss = []
accuracy = []
val_loss = []
val_accuracy = []

# Перевірка на успішне відкривання файлу
try:
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

        print(f"Файл успішно відкритий. Кількість рядків: {len(lines)}")

        # Форматування файлу, щоб всі необхідні дані були на одному рядку
        for i in range(0, len(lines), 2):
            # Обробляємо рядок з номером епохи
            epoch_line = lines[i].strip()
            # Обробляємо рядок з метриками
            data_line = lines[i + 1].strip()

            # Витягування номеру епохи
            epoch_match = epoch_pattern.search(epoch_line)
            if epoch_match:
                epoch = int(epoch_match.group(1))
                epochs.append(epoch)
            else:
                print(f"⚠️ Не вдалося знайти епоху в рядку: {epoch_line}")
                continue

            # Витягування метрик
            data_match = metrics_pattern.search(data_line)
            if data_match:
                loss_value = float(data_match.group(1))
                accuracy_value = float(data_match.group(2))
                val_loss_value = float(data_match.group(3))
                val_accuracy_value = float(data_match.group(4))

                loss.append(loss_value)
                accuracy.append(accuracy_value)
                val_loss.append(val_loss_value)
                val_accuracy.append(val_accuracy_value)

            else:
                print(f"⚠️ Не вдалося знайти метрики для епохи {epoch}: {data_line}")
                continue

except FileNotFoundError:
    print("❌ Помилка: Файл не знайдено.")
    exit()
except Exception as e:
    print(f"❌ Помилка при відкриванні файлу: {e}")
    exit()

# Перевірка наявності даних
if not epochs:
    print("❌ Помилка: Не вдалося знайти дані для побудови графіків. Перевірте формат файлу.")
    exit()


# Побудова графіків
plt.figure(figsize=(12, 6))

# Графік loss
plt.plot(epochs, loss, label="Train Loss", marker="o")
plt.plot(epochs, val_loss, label="Validation Loss", marker="o")
plt.title("Loss During Training")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)
plt.show()

# Графік accuracy
plt.figure(figsize=(12, 6))
plt.plot(epochs, accuracy, label="Train Accuracy", marker="o")
plt.plot(epochs, val_accuracy, label="Validation Accuracy", marker="o")
plt.title("Accuracy During Training")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(True)
plt.show()
