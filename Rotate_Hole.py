"""
Input: Two arguments.
A initial state as a list with 1 and/or 0
Pipe numbers for cannonballs as a list of integers
Output: The rotating variants as a list of integers or an empty list.
Example:
rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]) == [1, 8]
rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]) == []
rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]) == [0]
rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]) == [0, 5]
"""
def rotate(state, pipe_numbers):
    rotate_pass = []
    # create empty matrix pipe
    matrix_pipe = [0 for i in range(len(state))]
    # 1 - pipe have a bomb, 0 - don't have a bomb
    for i in pipe_numbers: matrix_pipe[i] = 1
    for j in range(len(state)):
        rotate_pass.append(j)
        if j == 0:
            pass
        else:
            # rotate matrix by clock ring
            temp = state.pop(-1)
            state.insert(0, temp)
        for i in range(len(matrix_pipe)):
            if matrix_pipe[i] == 1:
                if state[i] == 1:
                    continue
                else:
                    rotate_pass.pop(-1)
                    break
    return rotate_pass

# test
print(rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]))
