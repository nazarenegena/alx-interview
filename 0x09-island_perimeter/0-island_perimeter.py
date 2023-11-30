#!/usr/bin/python3
"""computing Island perimeter module.
"""


def island_perimeter(grid):
    """function for the perimeter of an island 
    """
    perimeter = 0
    if type(grid) != list:
        return 0
    num = len(grid)
    for i, row in enumerate(grid):
        mul = len(row)
        for k, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                i == 0 or (len(grid[i - 1]) > k and grid[i - 1][k] == 0),
                k == mul - 1 or (mul > k + 1 and row[k + 1] == 0),
                i == num - 1 or (len(grid[i + 1]) > k and grid[i + 1][k] == 0),
                k == 0 or row[k - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter