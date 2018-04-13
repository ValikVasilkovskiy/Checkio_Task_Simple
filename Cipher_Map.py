# Input: A cipher grille and a ciphered password as a tuples of strings.
# Output: The password as a string.
# Example: recall_password(('X...','..X.','X..X','....'),('itdf','gdce','aton','qrdi')) == 'icantforgetiddqd'

def recall_password(cipher_grille, ciphered_password):
    # in main_matrix add first element (not transform cipher_grille)
    stack, buffer_matrix, main_matrix, i = '', cipher_grille, [cipher_grille, ], 1
    # rotate three times (90 degrees) by arrow clock
    while i <= 3:
        # from the last column create new (buffer) matrix
        matrix_transform = list(zip(buffer_matrix[-1], buffer_matrix[-2], buffer_matrix[-3], buffer_matrix[-4]))
        main_matrix.append(matrix_transform)
        buffer_matrix = matrix_transform
        i += 1
    # all element compare with 'X'
    for i in range(len(main_matrix)):
        for j in range(len(main_matrix[i])):
            for r in range(len(main_matrix[i][j])):
                if main_matrix[i][j][r] == 'X':
                    # main matrix = 3 level [i][j][r], pass matrix = 2 level [j][r]
                    stack += ciphered_password[j][r]
    return stack
print(recall_password(('X...','..X.','X..X','....'),('itdf','gdce','aton','qrdi')))