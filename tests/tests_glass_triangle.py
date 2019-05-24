import unittest

from libs.complete_list_solution.glass import Glass
from libs.complete_list_solution.glass_triangle import GlassTriangle


class TestUsersSearch(unittest.TestCase):
    search_engine = None

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_small_volume_small_capacity(self):
        glass_triangle = GlassTriangle(5)
        glass_triangle.fill_triangle(39)
        actual = glass_triangle.get_as_list()
        expected = [[5], [5, 5], [5, 5, 5], [0.5, 4.0, 4.0, 0.5]]
        self.assertEqual(actual, expected)

    def test_large_volume_small_capacity(self):
        glass_triangle = GlassTriangle(25)
        glass_triangle.fill_triangle(1000)
        actual = glass_triangle.get_as_list()
        expected = [[25], [25, 25], [25, 25, 25], [25, 25, 25, 25], [25, 25, 25, 25, 25],
                    [7.03125, 25, 25, 25, 25, 7.03125], [0, 25, 25, 25, 25, 25, 0],
                    [0, 3.3203125, 25, 25, 25, 25, 3.3203125, 0], [0, 0, 14.84375, 25, 25, 25, 14.84375, 0, 0],
                    [0, 0, 0, 22.412109375, 25, 25, 22.412109375, 0, 0, 0],
                    [0, 0, 0, 0, 19.9462890625, 25, 19.9462890625, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 7.4462890625, 7.4462890625, 0, 0, 0, 0, 0]]
        self.assertEqual(actual, expected)

    def test_negative_volume(self):
        glass_triangle = GlassTriangle(25)
        self.assertRaises(ValueError, glass_triangle.fill_triangle, -1)

    def test_negative_glass_capacity(self):
        self.assertRaises(IndexError,Glass, 0, 0, -1)

    def test_volume_less_than_capacity(self):
        glass_triangle = GlassTriangle(25)
        glass_triangle.fill_triangle(20)
        actual = glass_triangle.get_as_list()
        expected = [[20]]

        self.assertEqual(actual, expected)

    def test_no_volume_to_pour(self):
        glass_triangle = GlassTriangle(25)
        glass_triangle.fill_triangle(0)
        actual = glass_triangle.get_as_list()
        expected = []
        self.assertEqual(actual, expected)

    def test_get_class_at_i_j(self):
        glass_triangle = GlassTriangle(5)
        glass_triangle.fill_triangle(100)
        actual = glass_triangle.get_glass_at_i_and_j(4,0)
        expected = '4,0 | 1.5625 ml | 31.200% full'

        self.assertEqual(str(actual), expected)



if __name__ == '__main__':
    unittest.main()
