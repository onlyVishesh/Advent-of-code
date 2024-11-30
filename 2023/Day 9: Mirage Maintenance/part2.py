# Taking input form file
with open('Day 9: Mirage Maintenance/test cases.txt', 'r') as file:
    input = [line.strip() for line in file]

# Function to check if all element in arr is zero or not
def checkAllZero(arr):
    flag = False
    for i in arr:
        if (i!=0):
            flag = True
            break
    return flag

count = 0
for i in input:
    list = []
    list.append([eval(p) for p in i.split()])
    q=0
    # Creating array according to question logic to predict future value
    while(checkAllZero(list[q])):
        list.append([])
        for j in range(len(list[q])-1):
            list[q+1].append(int(list[q][j+1])-int(list[q][j]))
        q+=1
        
    firstValue = 0

    # Predicting future value
    while(q!=0):
        firstValue = list[q-1][0]-list[q][0]
        list[q-1].insert(0,firstValue)
        q-=1

    count += list[0][0]
    # print(list,q)

print(count)