def getTotalpopulation(cities):
    total = 0
    for i in range(len(cities)):
        entry=cities[i]
        total = total + entry[2]
    return total
print(getTotalpopulation([ ["Pittsburgh", "Allegheny", 302407],
           ["Philadelphia", "Philadelphia", 1584981],
           ["Allentown", "Lehigh", 123838],
           ["Erie", "Erie", 97639],
           ["Scranton", "Lackawanna", 77182] ]))#function call 1
