
with open('Day 4: Ceres Search/test cases.txt', 'r') as file:
    lines = [line for line in file]
    grid = [list(row) for row in lines]


def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    word = "XMAS"
    word_length = len(word)
    directions = [
        (0, 1),   
        (0, -1),  
        (1, 0),   
        (-1, 0),  
        (1, 1),   
        (-1, -1), 
        (1, -1),  
        (-1, 1), 
    ]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def find_word(x, y, dx, dy):
        for k in range(word_length):
            nx, ny = x + k * dx, y + k * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[k]:
                return False
        return True

    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == word[0]:  
                for dx, dy in directions:
                    if find_word(i, j, dx, dy):
                        count += 1

    return count

# Count occurrences of XMAS
xmas_count = count_xmas(grid)
print(xmas_count)
