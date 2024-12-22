from Example import example
from Dijkstra import dijkstra

city = example().makeexamplecity()
calcmodel = dijkstra(city)
distrikt_value = dict()

for elem in city.edges:
    distances = calcmodel.dijkstra(elem)
    distrikt_value[elem] = 0
    for district in distances:
        if elem == district:
            distrikt_value[elem] += city.get_importance(district)
        else:    
            distrikt_value[elem] += city.get_importance(district)/distances[district]

district_priority = sorted(distrikt_value.items(), key=lambda item: -item[1])

for el in district_priority:
    print(f"District: {el[0]} value: {el[1]} \n")