"""
Input: A matrix as a list of lists with integers.
Output: Whether or not a sequence exists as a boolean.
Example:
sequence([
    [1, 2, 1, 1],
    [1, 1, 4, 1],
    [1, 3, 1, 6],
    [1, 7, 2, 5]
]) == True
sequence([
    [7, 1, 4, 1],
    [1, 2, 5, 2],
    [3, 4, 1, 3],
    [1, 1, 8, 1]
]) == False
"""
def check_sequence_line(line):
    seq_count = 1
    if len(line) <= 3:
        return False
    for i in range(1, len(line)):
        if line[0] == line[i]:
            seq_count += 1
            if seq_count == 4:
                return True
        else:
            return False
    return False

def sequence(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # create vertical line
            column_line = []
            list(map(lambda v: column_line.append(v[j]), matrix[i:]))
            # create diagonal line
            diagonal_line = []
            dj = 0
            for d in range(i, len(matrix)):
                try:
                    diagonal_line.append(matrix[d][j + dj])
                    dj += 1
                except IndexError:
                    break
            # create inverse diagonal line
            inverse_diagonal_line = []
            idj = 0
            for id in range(i, len(matrix)):
                try:
                    # j only > 0 (positive value)
                    if j - idj < 0:
                        break
                    inverse_diagonal_line.append(matrix[id][j - idj])
                    idj += 1
                except IndexError:
                    break
            # check horizontal line for point
            if check_sequence_line(matrix[i][j:]):
                return True
            # check vertical line for point
            elif check_sequence_line(column_line):
                return True
            # check diagonal line for point
            elif check_sequence_line(diagonal_line):
                return True
            # check inverse diagonal line for point
            elif check_sequence_line(inverse_diagonal_line):
                return True
    return False

#test
print(sequence([[2,6,2,3,5,2,4,8,7],
                [5,7,8,5,9,5,7,3,4],
                [6,4,1,2,1,6,5,8,5],
                [9,3,1,3,5,4,6,4,8],
                [9,6,6,8,1,9,1,2,1],
                [5,5,5,8,6,5,3,2,5],
                [7,5,2,9,2,9,8,2,5],
                [5,8,1,9,1,2,6,2,2],
                [7,5,3,6,1,6,9,5,9]]))