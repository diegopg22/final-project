import data
from main import average_waste, food_waste_gt, food_waste_lt, feedback
import unittest

#cities for sample testing

city1 = data.City('Panama City', 'Panama', 1300000, 101)
city2 = data.City('Bogota', 'Columbia', 7400000,70)
city3 = data.City('Caye Caulker', 'Belize', 1600, 45)

cities = [city1, city2, city3]
class Testcases(unittest.TestCase):
    pass

    #average waste test
    def test_average_waste_1(self):
        result = average_waste(cities)
        expected = 72.0
        self.assertAlmostEqual(result, expected)

    def test_average_waste_2(self):
        lst = [city1, city3]
        result = average_waste(lst)
        expected = 73.0
        self.assertAlmostEqual(result, expected)

    #food waste test
    def test_food_waste_gt_1(self):
        result = food_waste_gt(cities)
        expected = [city1]
        self.assertEqual(result, expected)

    def test_food_waste_gt_2(self):
        lst = [city2, city3]
        result = food_waste_gt(lst)
        expected = [city2]
        self.assertEqual(result, expected)

    #food waste less than
    def test_food_waste_lt_1(self):
        result = food_waste_lt(cities)
        expected= [city2, city3]
        self.assertEqual(result, expected)

    def test_food_waste_lt_2(self):
        lst = [city1]
        result = food_waste_lt(lst)
        expected = [city1]
        self.assertEqual(result, expected)

