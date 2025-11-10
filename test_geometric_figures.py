import unittest
import math
from circle import area as circle_area, perimeter as circle_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter


class TestCircle(unittest.TestCase):
    
    def test_circle_area_zero_radius(self):
        self.assertEqual(circle_area(0), 0)
    
    def test_circle_area_positive_radius(self):
        self.assertAlmostEqual(circle_area(5), math.pi * 25)
    
    def test_circle_area_large_radius(self):
        self.assertAlmostEqual(circle_area(10), math.pi * 100)
    
    def test_circle_perimeter_zero_radius(self):
        self.assertEqual(circle_perimeter(0), 0)
    
    def test_circle_perimeter_positive_radius(self):
        self.assertAlmostEqual(circle_perimeter(5), 2 * math.pi * 5)
    
    def test_circle_perimeter_large_radius(self):
        self.assertAlmostEqual(circle_perimeter(10), 2 * math.pi * 10)


class TestRectangle(unittest.TestCase):
    
    def test_rectangle_area_zero_sides(self):
        self.assertEqual(rectangle_area(0, 5), 0)
        self.assertEqual(rectangle_area(5, 0), 0)
        self.assertEqual(rectangle_area(0, 0), 0)
    
    def test_rectangle_area_positive_sides(self):
        self.assertEqual(rectangle_area(5, 3), 15)
        self.assertEqual(rectangle_area(10, 4), 40)
    
    def test_rectangle_area_square(self):
        self.assertEqual(rectangle_area(4, 4), 16)
    
    def test_rectangle_perimeter_zero_sides(self):
        self.assertEqual(rectangle_perimeter(0, 5), 10)
        self.assertEqual(rectangle_perimeter(5, 0), 10)
        self.assertEqual(rectangle_perimeter(0, 0), 0)
    
    def test_rectangle_perimeter_positive_sides(self):
        self.assertEqual(rectangle_perimeter(5, 3), 16)
        self.assertEqual(rectangle_perimeter(10, 4), 28)
    
    def test_rectangle_perimeter_square(self):
        self.assertEqual(rectangle_perimeter(4, 4), 16)


class TestSquare(unittest.TestCase):
    
    def test_square_area_zero_side(self):
        self.assertEqual(square_area(0), 0)
    
    def test_square_area_positive_side(self):
        self.assertEqual(square_area(5), 25)
        self.assertEqual(square_area(10), 100)
    
    def test_square_perimeter_zero_side(self):
        self.assertEqual(square_perimeter(0), 0)
    
    def test_square_perimeter_positive_side(self):
        self.assertEqual(square_perimeter(5), 20)
        self.assertEqual(square_perimeter(10), 40)


class TestTriangle(unittest.TestCase):
    
    def test_triangle_area_zero_base_height(self):
        self.assertEqual(triangle_area(0, 5), 0)
        self.assertEqual(triangle_area(5, 0), 0)
        self.assertEqual(triangle_area(0, 0), 0)
    
    def test_triangle_area_positive_base_height(self):
        self.assertEqual(triangle_area(6, 4), 12)
        self.assertEqual(triangle_area(10, 5), 25)
    
    def test_triangle_perimeter_zero_sides(self):
        self.assertEqual(triangle_perimeter(0, 0, 0), 0)
        self.assertEqual(triangle_perimeter(5, 0, 0), 5)
    
    def test_triangle_perimeter_positive_sides(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)
        self.assertEqual(triangle_perimeter(5, 5, 5), 15)
    
    def test_triangle_perimeter_equilateral(self):
        self.assertEqual(triangle_perimeter(6, 6, 6), 18)


if __name__ == '__main__':
    unittest.main()