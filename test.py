import unittest
import example


class TestCase(unittest.TestCase):

    def test_add_1(self):
        self.assertEqual(example.add(1, 2), 3)

    def test_sub_1(self):
        self.assertEqual(example.sub(3, 1), 2)

    def test_mult_1(self):
        self.assertEqual(example.mult(2, 2), 4)

    def test_div_1(self):
        self.assertEqual(example.div(6, 2), 3)


if __name__ == '__main__':
    unittest.main()
