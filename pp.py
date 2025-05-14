# Створення віртуального середовища (опціонально, але рекомендовано)
python3.6 -m venv .venv

# Активація віртуального середовища
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Встановлення необхідних бібліотек
pip install opencv-python Pillow numpy

# Запуск програми
python image_filter.py