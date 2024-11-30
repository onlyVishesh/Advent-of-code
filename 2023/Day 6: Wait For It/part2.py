import fileinput

list = []


for line in fileinput.input(files ='Day 6: Wait For It/test cases.txt'):
  line = str(line)
  line = line.split(":")
  line = line[1].split()

  list.append(line)


count = 0
t = ""
dis = ""
for i in range(len(list[0])):
  t = t + list[0][i]
  dis += list[1][i]

time = int(t)
dis = int(dis)

for j in range(14,int(t)):
  if(j*(time-j)>dis):
    count+=1


print(count)