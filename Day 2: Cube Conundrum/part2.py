import fileinput
count = 0

list = []
# taking input form text file and storing it in list and modifying it according to me
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

  r=0
  b=0
  g=0
  
  # finding max value of r, g and b
  for i in range(len(line[1])):
    for j in range(len(line[1][i])):
      if(line[1][i][j].split()[1]=="red"):
        if(int(line[1][i][j].split()[0])>r):
          r = int(line[1][i][j].split()[0])
          
      if(line[1][i][j].split()[1]=="green"):
        if(int(line[1][i][j].split()[0])>g):
          g = int(line[1][i][j].split()[0])
    
      if(line[1][i][j].split()[1]=="blue"):
        if(int(line[1][i][j].split()[0])>b):
          b = int(line[1][i][j].split()[0])

  count += r*g*b
    
print(count)