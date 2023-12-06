import fileinput, re
count = 0

# taking input form text file and storing it in list
list = []
for line in fileinput.input(files ='Advent of code solution/Day 3: Gear Ratios/test cases.txt'):
    line = str(line)[:-1]
    list.append(line)

# regex function to find special character in string
def regex(string):
    regex = re.compile('[*]')   
    if(regex.search(string) != None):
        return True
    else:
        return False  
arr1 = []
arr2 = []

# this function add num and its * index to arr1 and arr2 respectively
def addNum(num,i,j):
    if(num in arr1):
      arr2[arr1.index(num)].append([i,j])
    else:
      arr1.append(num)
      arr2.append([[i,j]])

# extracting number one by one form input
for i in range(len(list)):
  num = ""
  digit = 0
  list[i]+="."
  for j in range(len(list[i])):
    if(list[i][j]>="0" and list[i][j]<="9"):
      num+=list[i][j]
      digit+=1
    elif(digit != 0):
      start = j-digit-1
      end = j
      if(i==0):
         if(start != -1 and regex(list[i][start])):
           addNum(num,i,start)
         elif(start != -1 and regex(list[i+1][start])):
           addNum(num,i+1,start)
         elif(end != len(list[i])-1 and regex(list[i][end])):
           addNum(num,i,end)
         elif(end != len(list[i])-1 and regex(list[i+1][end])):
           addNum(num,i+1,end)
         else:
            for p in range(start,end):
               if(regex(list[i+1][p])):
                  addNum(num,i+1,p)
      elif(i==len(list)-1):
         if(start != -1 and regex(list[i-1][start])):
           addNum(num,i-1,start)
         elif(start != -1 and regex(list[i][start])):
           addNum(num,i,start)
         elif(end != len(list[i])-1 and regex(list[i-1][end])):
           addNum(num,i-1,end)
         elif(end != len(list[i])-1 and regex(list[i][end])):
           addNum(num,i,end)
         else:
            for p in range(start,end):
               if(regex(list[i-1][p])):
                  addNum(num,i-1,p)
      else:
         if(start != -1 and regex(list[i][start])):
           addNum(num,i,start)
         elif(start != -1 and regex(list[i-1][start])):
           addNum(num,i-1,start)
         elif(start != -1 and regex(list[i+1][start])):
           addNum(num,i+1,start)
         elif(end != len(list[i])-1 and regex(list[i][end])):
           addNum(num,i,end)
         elif(end != len(list[i])-1 and regex(list[i-1][end])):
           addNum(num,i-1,end)
         elif(end != len(list[i])-1 and regex(list[i+1][end])):
           addNum(num,i+1,end)
         else:
            for p in range(start+1,end):
               if(regex(list[i-1][p])):
                  addNum(num,i-1,p)
            for p in range(start+1,end):
               if(regex(list[i+1][p])):
                  addNum(num,i+1,p)
      # print(num)
      num = ""
      digit = 0

# converting arr1 and arr2 in dictionary
dict={}
for i in range(len(arr1)):
   dict[arr1[i]] = arr2[i]

# print(dict)

# extracting all the keys
keys = []
for i in dict:
   keys.append(i)

# iterating over keys of dict
for key1 in range(len(keys)):
   for key2 in range(key1+1,len(keys)):
      # iterating over values of key1, key2 in dict and checking if two no. have same "*" indices
      for i in dict[keys[key1]]:
        for j in dict[keys[key2]]:
            if(i==j):
              count+= int(keys[key1])*int(keys[key2])

# print(arr1, arr2)
# print(keys)
print(int(count))
      