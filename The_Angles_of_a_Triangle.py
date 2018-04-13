"""
Input: The lengths of the sides of a triangle as integers.
Output: Angles of a triangle in degrees as sorted list of integers.
Example:
angle_of_a_triangle(4, 4, 4) == [60, 60, 60]
angle_of_a_triangle(3, 4, 5) == [37, 53, 90]
angle_of_a_triangle(2, 2, 5) == [0, 0, 0]

"""

import math
def angle_of_a_triangle(a, b, c):
    stack = []
    if a + b > c and a + c > b and b + c > a:
        # math.degrees convert radian to angles
        stack.append(round(math.degrees(math.acos(((b ** 2) + (c ** 2) - (a ** 2)) / (2 * (c * b))))))
        stack.append(round(math.degrees(math.acos(((a ** 2) + (c ** 2) - (b ** 2)) / (2 * (a * c))))))
        stack.append(round(math.degrees(math.acos(((a ** 2) + (b ** 2) - (c ** 2)) / (2 * (a * b))))))
    else:
        return [0, 0, 0]
    stack.sort()
    return stack

# test
print(angle_of_a_triangle(5, 4, 3))
