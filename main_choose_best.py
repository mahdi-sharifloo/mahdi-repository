from  roads import roads

def main():
    actions()







def actions():
    numberOfways = int(input("how many ways between citys ? "))

    for i in range(numberOfways):
        distanceInput=int(input("input distance of road "+str(i+1)+" :"))
        roadCollapse = int(input("input the road collapse (between 0 and 9) : "))
        roadtype = int(input("1)...     2)...   3)...   4)... \n  choose the road type : "))
        roads.listOfRoads[i] = roads(distanceInput,roadCollapse,roadtype)
    selectWay(roadtype)

def selectWay(roadtype):
    minVal = 100000000
    print(roads.listOfRoads)
    for i in range(0,len(roads.listOfRoads)):
        sumTribels = roads.listOfRoads[i].distance + roads.listOfRoads[i].collapse
        print(sumTribels)
        if minVal>sumTribels:
            minVal = sumTribels

    if roadtype==1:
        pass
    elif roadtype==2:
        pass
    elif roadtype==3:
        pass
    elif roadtype==4:
        pass
    else:
        print("we have not this road type")

    print(minVal)







if __name__ == '__main__': main()

