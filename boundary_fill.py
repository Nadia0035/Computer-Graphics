def boundary_fill(grid, x, y, fill_color, boundary_color):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
        return

    if grid[x][y] != boundary_color and grid[x][y] != fill_color:
        grid[x][y] = fill_color

        
        # Explore 4 directions
        boundary_fill(grid, x + 1, y, fill_color, boundary_color)
        boundary_fill(grid, x - 1, y, fill_color, boundary_color)
        boundary_fill(grid, x, y + 1, fill_color, boundary_color)
        boundary_fill(grid, x, y - 1, fill_color, boundary_color)
grid = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1]
]

# Start from a point that's not a boundary (e.g., inside the region)
start_x, start_y = 1, 1
boundary_color = 1
fill_color = 2

boundary_fill(grid, start_x, start_y, fill_color, boundary_color)

# Print result
for row in grid:
    print(row)
