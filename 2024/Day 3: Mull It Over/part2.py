import re



# Read input from file
with open('2024/Day 3: Mull It Over/test cases.txt', 'r') as file:
    memories = [line.strip() for line in file]

# Define regex patterns
mul_pattern = r'mul\(\d{1,3},\d{1,3}\)'
do_pattern = r'do\(\)'
dont_pattern = r"don't\(\)"

# Initialize variables
mul_enabled = True  # `mul()` instructions are initially enabled
total_sum = 0

# Process each line in the corrupted memory
for memory in memories:
    # Split the memory into components using regex
    instructions = re.findall(rf'{mul_pattern}|{do_pattern}|{dont_pattern}', memory)
    
    for instruction in instructions:
        if re.match(do_pattern, instruction):
            mul_enabled = True
        elif re.match(dont_pattern, instruction):
            mul_enabled = False
        elif re.match(mul_pattern, instruction):
            if mul_enabled:
                # Extract numbers from the mul() instruction
                x, y = map(int, instruction[4:-1].split(","))
                total_sum += x * y

# Output the result
print(total_sum)
