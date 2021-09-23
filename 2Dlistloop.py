cities = [["India","Hyderabad",54000,"extra"],["America","NewJersey",34000],["Austrilia","canberra",70000],["Britian","London",50000]]
for i in range(len(cities)):
    info = " "
    for j in range(len(cities[i])):
        if(j!=len(cities[i])-1):
            print(cities[i][j],end=" , ")
        else:
            print(cities[i][j],end=" ")
    print()
