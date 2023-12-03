import fileinput, re

# taking input form text file and storing it in list
list = []
for line in fileinput.input(files ='Day 1: Trebuchet/test cases.txt'):
    line = str(line)[:-1]
    list.append(line)

# Creating a regex to check if string has and digit or not
def regex(string):
    regex = re.compile('[0-9]')   
    if(regex.search(string) != None):
        return True
    else:
        return False
        
# Extracting digits from string
count = 0
for i in range(len(list)):
    temp = ""
    for j in range(len(list[i])):
        if(regex(list[i][j])):
            temp += list[i][j]
    # Checking if temp is not empty and adding a two digit no. to count (two digit = first digit and last digit of temp)
    if(temp!=""):
        count += int(f"{temp[0]}{temp[-1]}")

# Displaying total
print(count)