import re

with open('2024/Day 3: Mull It Over/test cases.txt', 'r') as file:
    memories = [line.strip() for line in file]

# Define the regex pattern
pattern = r'mul\(\d{1,3},\d{1,3}\)'

# Check matches
sum = 0
for memory in memories:
    # Split the memory into components using regex
    instructions = re.findall(pattern, memory)
    if len(instructions) > 1:
        for instruction in instructions:
            x,y = list(map(int,instruction[4:-1].split(",")))
            sum+=x*y

    

print(sum)