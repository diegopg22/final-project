def __init__(self, city_name, country, population, food_waste_per_capita):
    self.city_name = city_name
    self.country = country
    self.population = population
    self.food_waste_per_capita = food_waste_per_capita

def __repr__(self):
    return "{}, {} | Population: {} | Food Waste per Capita: {}".format(
        self.city_name,
        self.country,
        self.population,
        self.food_waste_per_capita
    )

#finds the average waste per capita per for the city
def average_waste(self):


#returns all cities with food waste per capita above the average
def food_waste_gt(self, average):
