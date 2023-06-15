#!/usr/bin/python3
import unittest
from models.base import Base
"""Test Base class"""


class TestBase(unittest.TestCase):
    def test_no_args(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b2.id, b3.id - 1)

    def test_id_public(self):
        b1 = Base()
        b1.id = 5
        self.assertEqual(b1.id, 5)

    def test_id_private(self):
        b1 = Base()
        with self.assertRaises(AttributeError):
            print(b1.__nb_objects)

    def test_id_string(self):
        b1 = Base("id")
        self.assertEqual(b1.id, "id")

    def test_id_negative(self):
        self.assertEqual(Base(-5).id, -5)

    def test_id_float(self):
        self.assertEqual(Base(5.5).id, 5.5)

    def test_id_list(self):
        self.assertEqual(Base([1, 2, 3]).id, [1, 2, 3])

    def test_id_tuple(self):
        self.assertEqual(Base((1, 2, 3)).id, (1, 2, 3))

    def test_range_id(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_unique_id(self):
        b1 = Base()
        b2 = Base()
        self.assertNotEqual(b1.id, b2.id)
