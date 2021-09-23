def getcountryname(cities,cityname):
    for i in range(len(cities)):
        entry=cities[i]
        if entry[1]==cityname:
            return entry[0]
    #return None
print(getcountryname([["India","Hyderabad",54000],["America","NewJersey",34000],["Austrilia","canberra",70000],["Britian","London",50000]],"Delhi"))