def checkio(land_map):
    stack = []
    def dfs(row, col):
        land_map[row][col] = 2
        counter = 1
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                # only in map
                if (i < 0) or (j < 0):
                    continue
                else:
                    try:
                        if land_map[i][j] != 2 and land_map[i][j] == 1:
                            counter += dfs(i, j)
                    except IndexError:
                        continue
        return counter
    for i in range(len(land_map)):
        for j in range(len(land_map[i])):
            if land_map[i][j] == 1:
                stack.append(dfs(i, j))
    stack.sort()
    return stack

assert checkio([[0, 0, 0, 0, 0, 0],
                [1, 0, 0, 1, 1, 1],
                [1, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0]]) == [2, 3, 3, 4]

assert checkio([[0, 0, 0, 0, 0],
                [0, 0, 1, 1, 0],
                [0, 0, 0, 1, 0],
                [0, 1, 1, 0, 0]]) == [5]

assert checkio([[0, 0, 0, 0, 0],
                [0, 0, 1, 1, 0],
                [0, 0, 0, 1, 0],
                [0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0]]) == [1, 3]



