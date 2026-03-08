import data
#finds the average waste per capita for all the cities in a list
def average_waste(lst: list[data.City]) -> float:
    count = 0
    total_waste = 0
    for cities in lst:
        total_waste += cities.food_waste_per_capita
        count += 1
    avg_waste = total_waste / count
    return avg_waste


#returns all cities with food waste per capita above the average
def food_waste_gt(lst: list[data.City]) -> list[data.City]:
    avg_waste = average_waste(lst)
    new_lst = []
    for cities in lst:
        if cities.food_waste_per_capita > avg_waste:
            new_lst.append(cities)
    return new_lst


#returns all cities with food waste per capita below and at the average
def food_waste_lt(lst: list[data.City]) -> list[data.City]:
    avg_waste = average_waste(lst)
    new_lst = []
    for cities in lst:
        if cities.food_waste_per_capita <= avg_waste:
            new_lst.append(cities)
    return new_lst


#gives feedback based on amount of food waste per capita and how that compares to the average
def feedback(lst: list[data.City]) -> None:
    avg = average_waste(lst)
    gt_avg = food_waste_gt(lst)
    lt_avg = food_waste_lt(lst) #Cities that are lower than average and at the average
    for cities in lst:
        print("Average Food Waste Per Capita:",avg,
              "\n{} Food Waste Per Capita:".
              format(cities.city_name), cities.food_waste_per_capita)
        if cities in lt_avg:
            print("Well Done, {}! Keep up the good work in keeping food waste low.\n".
                  format(cities.city_name))
        elif cities in gt_avg:
            print("Your food waste is above average, {}!\n"
                  "Some ways to reduce food waste are encourage residents and business to buy just as much as they need.\n"
                  "Additionally, setting up donation centers and composting can further encourage less food waste and promote a circular economy.\n".
                  format(cities.city_name))

if __name__ == '__main__':
    feedback(data.cities)