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
    
# checking if number in alphabetic form present
for i in range(len(list)):
    for j in range(0,len(list[i])):
      if(list[i][j:j+3] == "one"):
        list[i] = list[i].replace("one","1ne",1)
      elif(list[i][j:j+3] == "two"):
        list[i] = list[i].replace("two","2wo",1)
      elif(list[i][j:j+5] == "three"):
        list[i] = list[i].replace("three","3hree",1)
      elif(list[i][j:j+4] == "four"):
        list[i] = list[i].replace("four","4our",1)
      elif(list[i][j:j+4] == "five"):
        list[i] = list[i].replace("five","5ive",1)
      elif(list[i][j:j+3] == "six"):
        list[i] = list[i].replace("six","6ix",1)
      elif(list[i][j:j+5] == "seven"):
        list[i] = list[i].replace("seven","7even",1)
      elif(list[i][j:j+5] == "eight"):
        list[i] = list[i].replace("eight","8ight",1)
      elif(list[i][j:j+4] == "nine"):
        list[i] = list[i].replace("nine","9ine",1)
        
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