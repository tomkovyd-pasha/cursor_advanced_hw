import unittest
from functions_to_test import Calculator


class TestCalculator(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(Calculator.add(1, 5), 6)
        self.assertEqual(Calculator.add(1.2446, 5.2884), 6.533)
        self.assertEqual(Calculator.add([1, 2, 4], [2, 5, 7]), [1, 2, 4, 2, 5, 7])
        self.assertEqual(Calculator.add((1, 2, 4), (2, 5, 7)), (1, 2, 4, 2, 5, 7))
        self.assertEqual(Calculator.add("tex1_1", "text_2"), "tex1_1text_2")
        self.assertRaises(TypeError, Calculator.add, 1, "5")
        self.assertRaises(TypeError, Calculator.add, "1", 5)
        self.assertRaises(TypeError, Calculator.add, 1, "5")
        self.assertRaises(TypeError, Calculator.add, None, 5)
        self.assertRaises(TypeError, Calculator.add, 5, None)
        self.assertRaises(TypeError, Calculator.add, None, None)
        self.assertRaises(TypeError, Calculator.add, {1, 2, 4}, {2, 5, 7})
        self.assertRaises(TypeError, Calculator.add, [1, 2, 4], {2, 5, 7})
        self.assertRaises(TypeError, Calculator.add, {1, 2, 4}, [2, 5, 7])
        self.assertRaises(TypeError, Calculator.add, {"a": 2, "b": 1}, {"a": 2, "b": 1})

    def test_subtract(self) -> None:
        self.assertEqual(Calculator.subtract(1, 5), -4)
        self.assertEqual(Calculator.subtract(1.2446, 5.2884), -4.0438)
        self.assertEqual(Calculator.subtract({1, 2, 4}, {2, 5, 7}), {1, 4})
        self.assertEqual(Calculator.subtract({2, 5, 7}, {1, 2, 4}), {5, 7})
        self.assertRaises(TypeError, Calculator.subtract, "tex1_1", "text_2")
        self.assertRaises(TypeError, Calculator.subtract, 1, "5")
        self.assertRaises(TypeError, Calculator.subtract, "1", 5)
        self.assertRaises(TypeError, Calculator.subtract, 1, "5")
        self.assertRaises(TypeError, Calculator.subtract, None, 5)
        self.assertRaises(TypeError, Calculator.subtract, 5, None)
        self.assertRaises(TypeError, Calculator.subtract, None, None)
        self.assertRaises(TypeError, Calculator.subtract, {1, 2, 4}, [2, 5, 7])
        self.assertRaises(TypeError, Calculator.subtract, [1, 2, 4], [2, 5, 7])
        self.assertRaises(TypeError, Calculator.subtract, {"a": 2, "b": 1}, {"a": 2, "b": 1})

    def test_multiply(self) -> None:
        self.assertEqual(Calculator.multiply(1, 5), 5)
        self.assertEqual(Calculator.multiply(1.2446, 5.2884), 6.58194264)
        self.assertEqual(Calculator.multiply("a", 4), "aaaa")
        self.assertEqual(Calculator.multiply([1, 2], 2), [1, 2, 1, 2])
        self.assertEqual(Calculator.multiply((1, 2), 2), (1, 2, 1, 2))
        self.assertRaises(TypeError, Calculator.multiply, "a", 4.532)
        self.assertRaises(TypeError, Calculator.multiply, 4.532, "a")
        self.assertRaises(TypeError, Calculator.multiply, {1, 2}, 2)
        self.assertRaises(TypeError, Calculator.multiply, {1, 2}, None)
        self.assertRaises(TypeError, Calculator.multiply, [1, 2], None)
        self.assertRaises(TypeError, Calculator.multiply, {"a": 2, "b": 1}, 2)
        self.assertRaises(TypeError, Calculator.multiply, None, None)

    def test_divide(self) -> None:
        self.assertEqual(Calculator.divide(1, 5), 0.2)
        self.assertEqual(Calculator.divide(0, 5), 0)
        self.assertEqual(Calculator.divide(1.2446, 5.2884), 0.23534528401785038)
        self.assertRaises(ValueError, Calculator.divide, 7, 0)
        self.assertRaises(TypeError, Calculator.divide, [1, 2], 7)
        self.assertRaises(TypeError, Calculator.divide, "[1, 2]", 7)
        self.assertRaises(ValueError, Calculator.divide, "[1, 2]", 0)
        self.assertRaises(ValueError, Calculator.divide, [1, 2], 0)
        self.assertRaises(TypeError, Calculator.divide, 7, None)
        self.assertRaises(TypeError, Calculator.divide, None, 7)
