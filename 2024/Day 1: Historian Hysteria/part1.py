import fileinput

# taking input form text file and storing it in list
list1 = []
list2 = []
for line in fileinput.input(files ='2024/Day 1: Historian Hysteria/test cases.txt'):
    line = list(map(int,str(line)[:-1].split()))
    list1.append(line[0])
    list2.append(line[1])

# sorting both list
list1.sort()
list2.sort()

# finding the distance between the locations
totalDistance=0
for locationID in range(len(list1)):
    totalDistance+=abs(list1[locationID]-list2[locationID])

print(totalDistance)