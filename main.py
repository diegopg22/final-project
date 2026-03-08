import data
#finds the average waste per capita per for the city
def average_waste(lst: list[data.City]) -> float:
    count = 0
    total_waste = 0
    for cities in lst:
        total_waste += cities.food_waste_per_capita
        count += 1



#returns all cities with food waste per capita above the average
def food_waste_gt(self, average):
