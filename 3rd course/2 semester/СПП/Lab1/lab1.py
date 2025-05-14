from math import sqrt
from unittest import TestCase, main
from unittest.mock import Mock

# --- Основна функція ---
def quadratic(a, b, c):
    d = b ** 2 - 4 * a * c

    if d < 0:
        return 'Result is complex'

    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)

    return (x1,) if d == 0 else (x1, x2)

# --- Юніт тести ---
class TestQuadratic(TestCase):
    def test_complex_roots(self):
        self.assertEqual(quadratic(1, 2, 3), 'Result is complex')

    def test_one_root(self):
        self.assertEqual(quadratic(1, -4, 4), (2.0,))

    def test_two_roots(self):
        self.assertEqual(quadratic(1, -6, 5), (5.0, 1.0))

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            quadratic(0, 1, 2)

# --- Мок-об'єкт ---
quadratic_mock = Mock()
quadratic_mock.return_value = (2.0, -0.5)

def test_mock():
    assert quadratic_mock(2, -3, -2) == (2.0, -0.5)
    quadratic_mock.assert_called_with(2, -3, -2)

# --- Додаткові тести з assert ---
def test_assert_complex_roots():
    assert quadratic(1, 2, 3) == 'Result is complex'

def test_assert_one_root():
    assert quadratic(1, -4, 4) == (2.0,)

def test_assert_two_roots():
    assert quadratic(1, -6, 5) == (5.0, 1.0)

# --- Запуск тестів ---
if __name__ == '__main__':
    test_mock()   # як у звіті одногрупника
    main()
