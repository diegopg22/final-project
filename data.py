

class City:
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
cities = [
    City('Rio de Janeiro', 'Brazil', 6700000, 94),
    City('San Miguel', 'Ecuador', 2470, 34),
    City('Santo Domingo', 'Ecuador', 334826, 158),
    City('Punta Hermosa', 'Peru', 23470, 91),
    City('Macusani', 'Peru', 11707, 84),
    City('Belize City', 'Belize', 53000, 34),
    City('San Pedro', 'Belize',12000, 36),
    City('Caye Caulker', 'Belize', 1600, 45),
    City('Salcedo Municipality', 'Dominican Republic', 35000, 207),
    City('Santo Domingo', 'Dominican Republic', 4000000, 113),
    City('Panama City', 'Panama', 1300000, 101),
    City('Bogota', 'Colombia', 7400000,70),
    City('Mexicali', 'Mexico', 1200000, 126),
    City('Berriozábal', 'Mexico', 64632, 71),
    City('Ensenada', 'Mexico', 330652, 129),
    City('Chacao', 'Venezuela', 64629, 93)
]
