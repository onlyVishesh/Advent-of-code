import fileinput

list = []
mult = 1

for line in fileinput.input(files ='Day 6: Wait For It/test cases.txt'):
  line = str(line)
  line = line.split(":")
  line = line[1].split()

  list.append(line)



for i in range(len(list[0])):
  count = 0
  time = int(list[0][i])
  dis = int(list[1][i])

  for j in range(1,time):
    if(j*(time-j)>dis):
      count+=1

  mult *=count
print(mult)