import fileinput
count = 0

# taking input form text file line by line and storing it in line and modifying it according to me
for line in fileinput.input(files ='Advent of code solution/Day 4: Scratchcards/test cases.txt'):
  line = str(line)[:-1]
  line = line.split(":")[1].split("|")
  line[0] = line[0].split()
  line[1] = line[1].split()
  
  # counting total matching no.
  sameCards = 1
  for i in line[0]:
    for j in line[1]:
      if(i == j):
        # if same card is one then num 1
        # if same card is two then num is 1 1 
        # if same card is three then num is 1 2^0 2^1
        # .
        # if same card is n then num is 1 2^0 2^1 .... 2^(n-2)
        num = sameCards if sameCards == 1 else (2**(sameCards-2))
        count+=num
        sameCards+=1

print(count)
