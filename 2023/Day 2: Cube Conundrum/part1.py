import fileinput
count = 0

# taking input form text file line by line and storing it in line and modifying it according to me
for line in fileinput.input(files ='Day 2: Cube Conundrum/test cases.txt'): 
  line = str(line)[:-1]
  line = line.split(":")
  line[0] = line[0].split()[1]
  line[1] = line[1].split(";")
  for i in range(len(line[1])):
    line[1][i] = line[1][i].split(",")
    for j in range(len(line[1][i])):
      line[1][i][j] = line[1][i][j].strip()
      # print(list) 

  flag = 0
  # checking if red > 12 or green > 13 or blue > 14 in any set
  for i in range(len(line[1])):
    for j in range(len(line[1][i])):
      if(line[1][i][j].split()[1]=="red"):
        if(int(line[1][i][j].split()[0])>12):
          flag=1
          
      if(line[1][i][j].split()[1]=="green"):
        if(int(line[1][i][j].split()[0])>13):
          flag=1
    
      if(line[1][i][j].split()[1]=="blue"):
        if(int(line[1][i][j].split()[0])>14):
          flag=1
  
  # if flag == 0 that meant case is possible
  if(flag==0):
    count+= int(line[0])

print(count)
