# Parse the grid into a dictionary of (y, x): character
data = open("Day 4: Ceres Search/test cases.txt").readlines()
H, W = len(data), len(data[0])-1  # H = height, W = width
grid = {(y, x): data[y][x] for y in range(H) for x in range(W)}

count = 0
for y, x in grid:
    if grid[y, x] == "A":  
        lr = grid.get((y-1, x-1), "") + grid.get((y+1, x+1), "")  
        rl = grid.get((y-1, x+1), "") + grid.get((y+1, x-1), "") 
        
        count += {lr, rl} <= {"MS", "SM"}

print(count)
