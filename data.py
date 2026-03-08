from multiprocessing.managers import view_type

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
    City('Rio de Janeiro', 'Brasil', 6700000, 94),
    City('San Miguel', 'Ecuador', 2470, 34),
    City('Punta Hermosa', 'Peru', 23470, 91),
    City('Belize City', 'Belize', 53000, 34),
    City('San Pedro', 'Belize',12000, 36),
    City('Salcedo Municipality', 'Dominican Republic', )

]
