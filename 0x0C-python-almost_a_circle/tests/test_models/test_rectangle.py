#!/usr/bin/python3
"""Defines unittests for models/rectangle.py.

Unittest classes:
    TestRectangleInitialization
    TestRectangleHeight
    TestRectangleWidth
    TestRectangleX
    TestRectangleY
"""
import unittest as ut
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_Initialization(ut.TestCase):
    """Unittest for testing instantiation of the Rectangle class."""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(1, 1, 1)
        r2 = Rectangle(1, 2, 3)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(1, 1, 1, 1)
        r2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        r = Rectangle(1, 1, 1, 1, 98549844468486)
        self.assertEqual(r.id, 98549844468486)

    def test_x_is_private(self):
        r1 = Rectangle(1, 1, 1, 1)
        with self.assertRaises(AttributeError):
            print(r1.__x)

    def test_y_is_private(self):
        r1 = Rectangle(1, 1, 1, 1)
        with self.assertRaises(AttributeError):
            print(r1.__y)

    def test_height_is_private(self):
        r1 = Rectangle(1, 1, 1, 1)
        with self.assertRaises(AttributeError):
            print(r1.__height)

    def test_height_is_private(self):
        r1 = Rectangle(1, 1, 1, 1)
        with self.assertRaises(AttributeError):
            print(r1.__height)

    def test_height_getter(self):
        r1 = Rectangle(1, 1, 1, 1)
        self.assertEqual(r1.height, 1)

    def test_height_setter(self):
        r1 = Rectangle(1, 1, 1, 1)
        r1.height = 10
        self.assertEqual(r1.height, 10)

    def test_height_getter(self):
        r1 = Rectangle(1, 1, 1, 1)
        self.assertEqual(r1.height, 1)

    def test_height_setter(self):
        r1 = Rectangle(1, 1, 1, 1)
        r1.height = 10
        self.assertEqual(r1.height, 10)

    def test_x_getter(self):
        r1 = Rectangle(1, 1, 1, 1)
        self.assertEqual(r1.x, 1)

    def test_x_setter(self):
        r1 = Rectangle(1, 1, 1, 1)
        r1.x = 10
        self.assertEqual(r1.x, 10)

    def test_y_getter(self):
        r1 = Rectangle(1, 1, 1, 1)
        self.assertEqual(r1.y, 1)

    def test_y_setter(self):
        r1 = Rectangle(1, 1, 1, 1)
        r1.y = 10
        self.assertEqual(r1.y, 10)


class TestRectangleWidth(ut.TestCase):
    """Unit tests for testing width of Rectangle class."""

    def test_width_is_None(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 1)

    def test_width_is_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("hello", 1)

    def test_width_is_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1.1, 1)

    def test_width_is_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)

    def test_width_is_complex(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(5), 2)

    def test_width_is_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"1": 2}, 2)

    def test_width_is_bool(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)

    def test_width_is_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2), 2)

    def test_width_is_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2}, 2)

    def test_width_is_nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 2)

    def test_width_is_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 2)

    def test_width_is_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 1)


class TestRectangleHeight(ut.TestCase):
    """Unit tests for testing height of Rectangle class."""

    def test_height_is_None(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_height_is_str(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "hello")

    def test_height_is_float(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 1.1)

    def test_height_is_list(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [2, 5, 8, 5])

    def test_height_is_complex(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, complex(5))

    def test_height_is_dict(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"1": 2})

    def test_height_is_bool(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, True)

    def test_height_is_tuple(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (1, 2))

    def test_height_is_set(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {1, 2})

    def test_height_is_nan(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, float('nan'))

    def test_height_is_inf(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('inf'))

    def test_height_is_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)


class TestRectangleX(ut.TestCase):
    """Unit tests for testing x of Rectangle class."""

    def test_x_is_None(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, None)

    def test_x_is_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, "hello")

    def test_x_is_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, "hello")

    def test_x_is_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2, 3])

    def test_x_is_complex(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 5, complex(5), 2)

    def test_x_is_dict(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, {"1": 2}, 2)

    def test_x_is_bool(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, True, 2)

    def test_x_is_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, (1, 2), 2)

    def test_x_is_set(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, {1, 2}, 2)

    def test_x_is_nan(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, float('nan'), 2)

    def test_x_is_inf(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, float('inf'), 2)

    def test_x_is_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 1, -1, 2)


class TestRectangleY(ut.TestCase):
    """Unit tests for testing x of Rectangle class."""

    def test_y_is_None(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, None)

    def test_y_is_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, "hello")

    def test_y_is_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, "hello")

    def test_y_is_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, [1, 2, 3])

    def test_y_is_complex(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 5, 1, complex(5))

    def test_y_is_dict(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, {"1": 2})

    def test_y_is_bool(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, True)

    def test_y_is_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, (1, 2))

    def test_y_is_set(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, {1, 2})

    def test_y_is_nan(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, float('nan'))

    def test_y_is_inf(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, float('inf'))

    def test_y_is_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 1, 1, -1)
