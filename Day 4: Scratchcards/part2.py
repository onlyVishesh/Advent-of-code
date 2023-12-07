import fileinput
list = []

# taking input form text file and storing it in list
for line in fileinput.input(files ='Advent of code solution/Day 4: Scratchcards/test cases.txt'):
  line = str(line)[:-1]
  line = line.split(":")[1].split("|")
  line[0] = line[0].split()
  line[1] = line[1].split()

  list.append(line)

# creating an dictionary with key as card no. and value 1 
dict = {}
for i in range(1,len(list)+1):
  dict[i]=1

# counting total matching no. and then adding same no of consecutive cards to dict
for i in range(len(list)):
  sameCards = 1
  for j in list[i][0]:
    for k in list[i][1]:
      if(j == k):
        sameCards+=1
  for sameCard in range(i+2, i+sameCards+1):
    dict[sameCard] += 1*dict[i+1]


#  counting total no. of cards
count = 0
for keys in dict:
  count+= dict[keys]

print(count)
