import data
from main import average_waste, food_waste_gt, food_waste_lt, feedback

#cities for sample testing

city1 = data.City('Panama City', 'Panama', 1300000, 101)
city2 = data.City('Bogota', 'Columbia', 7400000,70)
city3 = data.City('Caye Caulker', 'Belize', 1600, 45)

cities = [city1, city2, city3]

#average waste test
def test_average_waste():
    assert average_waste(cities) == 72

def test_average_waste_():
    lst = [city1, city3]
    assert average_waste(lst) == 73

#food waste test
def test_food_waste_gt():
    result = food_waste_gt(cities)
    assert result == [city1]

def test_food_waste_gt_():
    lst = [city2, city3]
    result = food_waste_gt(lst)
    assert result == [city2]

#food waste less than
def test_food_waste_lt():
    result = food_waste_lt(cities)
    assert result == [city2, city3]

def test_food_waste_lt_():
    lst = [city1]
    result = food_waste_lt(lst)
    assert result == [city1]

#feedback test
def test_feedback():
    feedback([city1, city2, city3])

