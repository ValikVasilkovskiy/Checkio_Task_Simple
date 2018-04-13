# Input: An opacity measurement as an integer.
# Output: The age of the ghost as an integer.
# Example: 1 year -- 10000 - 1 = 9999 (1 is a Fibonacci number).
# Example: 2 year -- 9999 - 2 = 9997 (2 is a Fibonacci number).

def ghosts_age(opacity):
    fibonacci = 0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711
    i, end_opacity, age = 1, 10000, 0
    while end_opacity != opacity:
        if i in fibonacci:
            end_opacity -= i
            age += 1
            i += 1
        else:
            end_opacity += 1
            age += 1
            i += 1
    return age
print(ghosts_age(9990))



