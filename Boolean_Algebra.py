def boolean(x, y, operation):
    if operation == "conjunction":
        if x == 1 and y == 1:
            return 1
        else:
            return 0
    elif operation == "disjunction":
        if x == 0 and y == 0:
            return 0
        else:
            return 1
    elif operation == "implication":
        if x == 0 and y == 0:
            return 1
        elif x == 1 and y == 0:
            return 0
        elif x == 0 and y == 1:
            return 1
        elif x == 1 and y == 1:
            return 1
    elif operation == "exclusive":
        if x == 0 and y == 0:
            return 0
        elif x == 1 and y == 0:
            return 1
        elif x == 0 and y == 1:
            return 1
        elif x == 1 and y == 1:
            return 0
    elif operation == "equivalence":
        if x == y:
            return x
        else:
            return 0

print(boolean(0, 1, "equivalence"))

