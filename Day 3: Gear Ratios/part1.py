import fileinput, re
count = 0

# taking input form text file and storing it in list
list = []
for line in fileinput.input(files ='Advent of code solution/Day 3: Gear Ratios/test cases.txt'):
    line = str(line)[:-1]
    list.append(line)

# regex function to find special character in string
def regex(string):
    regex = re.compile('[$&@%+/*#=-]')   
    if(regex.search(string) != None):
        return True
    else:
        return False  
    
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
        if(start != -1 and (regex(list[i][start]) or regex(list[i+1][start]))):
           count+=int(num)
        elif(end != len(list[i])-1 and (regex(list[i][end]) or regex(list[i+1][end]))):
           count+=int(num)
        elif(regex(list[i+1][start+1:end])):
           count+=int(num)
      elif(i==len(list)-1):
        if(start != -1 and (regex(list[i][start]) or regex(list[i-1][start]))):
           count+=int(num)
        elif(end != len(list[i])-1 and (regex(list[i][end]) or regex(list[i-1][end]))):
           count+=int(num)
        elif(regex(list[i-1][start+1:end])):
           count+=int(num)
      else:
        if(start != -1 and (regex(list[i][start]) or regex(list[i-1][start]) or regex(list[i+1][start]))):
           count+=int(num)
        elif(end != len(list[i])-1 and (regex(list[i][end]) or regex(list[i-1][end]) or regex(list[i+1][end]))):
           count+=int(num)
        elif(regex(list[i-1][start+1:end]) or regex(list[i+1][start+1:end])):
           count+=int(num)
      # print(num)
      num = ""
      digit = 0
      

print(count)
      