import os
os.system('cls' if os.name == 'nt' else 'clear')

""" 
Create a game of minesweeper where the function takes a grid of "#" and "-" and returns the same grid where each "-" is replaced by a number representing adjacent "#" to that index value

"""
def annotate_mines(grid):
    """
    Function annotate_mines(grid):
    Create a new grid the same size as original grid
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    new_grid = [[None] * cols for _ in range(rows)]

    # Search the grid by rows and columns to identify "#"
    for r in range(rows):
        for c in range(cols):
            # If a "#" is found, copy to new grid
            if grid[r][c] == "#":
                new_grid[r][c] = "#"
            # If "-" is identified, count adjacent mines with function
            # and convert count to a string then copy to new grid
            else:
                count = count_adjacent_mines(grid, r, c)
                new_grid[r][c] = str(count)
    # Return the new grid
    return new_grid

# Helper: count adjacent mines to r,c value with function
def count_adjacent_mines(grid, r, c):
    # Set initial count to 0
    count = 0
    # Offsets to visit all 8 neighbors
    neighbor_offsets = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),           ( 0, 1),
        ( 1, -1), ( 1, 0),  ( 1, 1),
    ]

    # For each dr,dc create var new_r and new_c 
    # IF is_in_bounds and the crawler finds "#" add 1 to the count, return count
    for dr, dc in neighbor_offsets:
        new_r, new_c = r + dr, c + dc
        if is_in_bounds(grid, new_r, new_c) and grid[new_r][new_c] == "#":
            count += 1

    return count

# Function to check whether a row/col combination is in the grid (not out of bounds)
def is_in_bounds(grid, r, c):
    # returns True if r is greater than 0 and less than number of rows
    # AND c is greater than 0 and less than number of columns
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])

if __name__ == "__main__":
# Create the grid where mines and numbers will lie
    game_grid = [ ["-", "-", "-", "#", "#"],
                ["-", "#", "-", "-", "-"],
                ["-", "-", "#", "-", "-"],
                ["-", "#", "#", "-", "-"],
                ["-", "-", "-", "-", "-"] ] 
    
    result = annotate_mines(game_grid)

    for row in result:
        print(row)

""" expected_output = [ ["1", "1", "2", "#", "#"],
                    ["1", "#", "3", "3", "2"],
                    ["2", "4", "#", "2", "0"],
                    ["1", "#", "#", "2", "0"],
                    ["1", "2", "2", "1", "0"] ]  """


