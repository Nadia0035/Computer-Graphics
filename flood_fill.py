def flood_fill(grid, x, y, new_color):
    original_color = grid[x][y]
    if original_color == new_color:
        return  # No need to fill
    row= len(grid)
    col= len(grid[0])
    def fill(x, y):
        if (x < 0 or x >= row or y < 0 or y >= col or grid[x][y] != original_color):
            return

        grid[x][y] = new_color

        # Recurse in 4 directions
        fill(x + 1, y)
        fill(x - 1, y)
        fill(x, y + 1)
        fill(x, y - 1)

    fill(x, y)


grid = [
    [1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1]
]

start_x, start_y = 1, 1  # Inside a region with color 2
new_color = 3

flood_fill(grid, start_x, start_y, new_color)

# Print result
for row in grid:
    print(row)


