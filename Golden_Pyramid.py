"""
Input: A pyramid as a tuple of tuples. Each tuple contains integers.
Output: The maximum possible sum as an integer.
Example:
count_gold((
    (1,),
    (2, 3),
    (3, 3, 1),
    (3, 1, 5, 4),
    (3, 1, 3, 1, 3),
    (2, 2, 2, 2, 2, 2),
    (5, 6, 4, 5, 6, 4, 3)
)) == 23
"""
def count_gold(pyramid):
    reversed_pyramid = []
    if len(pyramid) >= 2:
        # create reversed pyramid
        for i in reversed(pyramid): reversed_pyramid.append(list(i))
        for i in range(1, len(reversed_pyramid)):
            for j in range(len(reversed_pyramid[i])):
                if (reversed_pyramid[i][j] + reversed_pyramid[i-1][j]) > (reversed_pyramid[i][j] + reversed_pyramid[i-1][j+1]):
                    reversed_pyramid[i][j] = (reversed_pyramid[i][j] + reversed_pyramid[i-1][j])
                else:
                    reversed_pyramid[i][j] = (reversed_pyramid[i][j] + reversed_pyramid[i-1][j+1])
        return reversed_pyramid[-1][0]
    else:
        return pyramid[-1][0]

# test
print(count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4))))