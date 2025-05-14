import csv
import unittest
from math import sqrt

# --- Обробка CSV ---
def parse_csv(file_path):
    with open(file_path, newline='') as f:
        reader = csv.reader(f)
        return [row[:1] + list(map(int, row[1:])) for row in reader]

# --- Обчислення площ та периметрів ---
def get_circle_area(radius):
    return 3.14 * radius ** 2

def get_circle_circumference(radius):
    return 2 * 3.14 * radius

def get_triangle_area(side):
    return (sqrt(3) / 4) * side ** 2

def get_triangle_perimeter(side):
    return side * 3

def get_rectangle_area(a, b):
    return a * b

def get_rectangle_perimeter(a, b):
    return 2 * (a + b)

# --- Обчислення характеристик фігур ---
def process_figures(data):
    for shape in data:
        shape_type = shape[0]
        params = shape[1:]

        if shape_type == 'triangle':
            area = get_triangle_area(params[0])
            perim = get_triangle_perimeter(params[0])
        elif shape_type == 'square':
            area = get_rectangle_area(params[0], params[1])
            perim = get_rectangle_perimeter(params[0], params[1])
        elif shape_type == 'circle':
            area = get_circle_area(params[0])
            perim = get_circle_circumference(params[0])
        else:
            print(f'[WARN] Unknown figure: {shape_type}')
            continue

        print(f'{shape_type.title()} ({", ".join(map(str, params))}): '
              f'Area = {area:.2f}, Perimeter = {perim:.2f}')

# --- Тести ---
class GeometryTests(unittest.TestCase):

    def test_area_circle(self):
        self.assertAlmostEqual(get_circle_area(2), 12.56)

    def test_circumference_circle(self):
        self.assertAlmostEqual(get_circle_circumference(2), 12.56)

    def test_area_triangle(self):
        self.assertAlmostEqual(get_triangle_area(4), (sqrt(3) / 4) * 16)

    def test_perimeter_triangle(self):
        self.assertEqual(get_triangle_perimeter(5), 15)

    def test_area_rectangle(self):
        self.assertEqual(get_rectangle_area(6, 3), 18)

    def test_perimeter_rectangle(self):
        self.assertEqual(get_rectangle_perimeter(6, 3), 18)

    def test_csv_parsing(self):
        raw = [['circle', '5'], ['triangle', '3'], ['square', '2', '4']]
        expected = [['circle', 5], ['triangle', 3], ['square', 2, 4]]
        self.assertEqual(parse_csv_data(raw), expected)

# --- Альтернативна функція для мок-тестів / pytest
def parse_csv_data(fake_csv):
    return [row[:1] + list(map(int, row[1:])) for row in fake_csv]

# --- Точка входу ---
if __name__ == '__main__':
    dataset = parse_csv('lab2/csv.csv')
    process_figures(dataset)
    # Для запуску тестів — розкоментувати:
    # unittest.main()
