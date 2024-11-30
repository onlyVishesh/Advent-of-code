# taking test case input for file
with open('Day 8: Haunted Wasteland/test cases.txt', 'r') as file:
    input = [line.strip() for line in file]

# Converting input to desired format
for i in range(2,len(input)):
    input[i] = input[i].split(" = ")
    input[i][1] = input[i][1][1:-1].split(", ")

# Creating function to move left or right of current node
def moveLeft(node,arr):
  for i in range(2,len(arr)):
    if(arr[i][0] == node):
      return arr[i][1][0]
    
  
def moveRight(node,arr):
  for i in range(2,len(arr)):
    if(arr[i][0] == node):
      return arr[i][1][1]
    
# Assigning initial value
startingNode = "AAA"
currentNode = startingNode
count = 0

# print(input[0])

# looping till current node is "ZZZ"
while(currentNode != "ZZZ"):
  # Checking instruction and moving accordingly
  for i in input[0]:
    if(i == "R"):
        currentNode = moveRight(currentNode,input)
        # print(currentNode)
        count+=1
    elif(i == "L"):
        currentNode = moveLeft(currentNode,input)
        # print(currentNode)
        count+=1
    if(currentNode == "ZZZ"):
      break

print(count)