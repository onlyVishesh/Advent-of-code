import fileinput

# taking input form text file and storing it in list
list1 = []
list2 = []
for line in fileinput.input(files ='2024/Day 1: Historian Hysteria/test cases.txt'):
    line = list(map(int,str(line)[:-1].split()))
    list1.append(line[0])
    list2.append(line[1])


# finding unique locations from both the list
uniqueLocations = list(set(list2))
uniqueLocations.extend(list(set(list1)))

# counting number of locations
countOfLocation = {}
for i in range(len(uniqueLocations)):
    countOfLocation[uniqueLocations[i]] = list2.count(uniqueLocations[i])

# finding total distance
totalDistance=0
for locationID in range(len(list1)):
    totalDistance += list1[locationID]*countOfLocation[list1[locationID]]

print(totalDistance)