'''
def matrix_adjacency_to_list_adjacency(data):
    list_adjacency = []
    for i in list(zip(*data)):
        temp = []
        for j in range(len(i)):
            if i[j] == 1:
                temp.append(j)
        list_adjacency.append(temp)
    return list_adjacency
'''
data = [[0, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0]]
def dfs(row, col):
    data[row][col] = 2
    counter = 1
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            # only in map
            if (i < 0) or (j < 0):
                continue
            else:
                try:
                    if data[i][j] != 2 and data[i][j] == 1:
                        data[i][j] = 2
                        counter += dfs(i, j)
                except IndexError:
                    continue
    return counter

stack = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 1:
            stack.append(dfs(i, j))
print(stack)



