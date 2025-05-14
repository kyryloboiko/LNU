import unittest
from math import sqrt
from figures import Circle, Triangle, Square, Cube
from managers import FigureManager, FigureCreator

class TestShapes(unittest.TestCase):
    def test_circle(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 3.14 * 25)
        self.assertAlmostEqual(circle.perimetr(), 2 * 3.14 * 5)

    def test_triangle(self):
        triangle = Triangle(6)
        self.assertAlmostEqual(triangle.area(), (sqrt(3) / 4) * 36)
        self.assertEqual(triangle.perimetr(), 18)

    def test_square(self):
        square = Square(4, 5)
        self.assertEqual(square.area(), 20)
        self.assertEqual(square.perimetr(), 18)

    def test_cube(self):
        cube = Cube(3)
        self.assertEqual(cube.area(), 54)
        self.assertEqual(cube.perimetr(), 36)
        self.assertEqual(cube.volume(), 27)

class TestFigureCreator(unittest.TestCase):
    def setUp(self):
        self.fm = FigureManager()
        self.fm.add_figure('circle')(Circle)
        self.fm.add_figure('triangle')(Triangle)
        self.fm.add_figure('square')(Square)
        self.fm.add_figure('cube')(Cube)
        self.fc = FigureCreator(self.fm)

    def test_create_circle(self):
        self.assertIsInstance(self.fc.create_figure('circle', [5]), Circle)

    def test_invalid_figure(self):
        with self.assertRaises(ValueError):
            self.fc.create_figure('hexagon', [2])

if __name__ == "__main__":
    unittest.main()
