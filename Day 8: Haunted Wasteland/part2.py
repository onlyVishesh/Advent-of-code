# This codes give correct answer but takes alot of time 
# taking test case input for file
with open('Day 8: Haunted Wasteland/test cases.txt', 'r') as file:
    input = [line.strip() for line in file]

# Converting input to desired format
for i in range(2,len(input)):
    input[i] = input[i].split(" = ")
    input[i][1] = input[i][1][1:-1].split(", ")

# Creating function to All current node move left or right of All current node

def moveLeft(nodes,arr):
  for nodeIndex in range(len(nodes)):
    for i in range(2,len(arr)):
        if(arr[i][0] == nodes[nodeIndex]):
            nodes[nodeIndex] = arr[i][1][0]
            break
  return nodes
    
  
def moveRight(nodes,arr):
  for nodeIndex in range(len(nodes)):
    for i in range(2,len(arr)):
        if(arr[i][0] == nodes[nodeIndex]):
            nodes[nodeIndex] = arr[i][1][1]
            break
  return nodes

# Finding all starting node ie nodes end with A
startingNodes = []
for i in range(2,len(input)):
  if(input[i][0][-1] == "A"):
    startingNodes.append(input[i][0])


# Creating function to check if all current nodes end with Z or not
def checkEndingOfNodes(arr):
   for i in arr:
      if(i[-1]!="Z"):
        return True
    
   return False


# Assigning initial value
currentNodes = startingNodes
count = 0

# print(checkEndingOfNodes(currentNodes))

# Looping till all current node end with Z
while(checkEndingOfNodes(currentNodes)):
  # Checking instruction and moving accordingly
  for i in input[0]:
    # print(i)
    if(i == "R"):
      currentNodes = moveRight(currentNodes,input)
      count+=1
    elif(i == "L"):
      currentNodes = moveLeft(currentNodes,input)
      count+=1
    # print(currentNodes)
    if(not checkEndingOfNodes(currentNodes)):
      break
    # print(count)

print(count)