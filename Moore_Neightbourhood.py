def count_neighbours(grid, row, col):
    neighbor = 0
    # edit set to list [[]]
    list_grid = list(map(lambda i: list(i), grid))
    # [i][j] around
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            # only in map
            if (i < 0) or (j < 0):
                continue
            else:
                try:
                    if list_grid[i][j] == 1:
                        neighbor += 1
                # if index out of range
                except IndexError:
                    continue
    # point[i][j] don't count
    if list_grid[row][col] == 1:
        neighbor -= 1
    return neighbor
print(count_neighbours(((1, 1, 1),
                        (1, 1, 1),
                        (1, 1, 1),), 0, 2))



