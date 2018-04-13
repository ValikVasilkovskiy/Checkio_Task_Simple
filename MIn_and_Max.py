def max(*args, **kwargs):
    key = kwargs.get('key')
    try:
        iterator = iter(args[0])
        if len(args) > 1:
            iterator2 = iter(args[0][0])
    except TypeError:
        max_value = args[0]
        if kwargs.get('key'):
            for i in args:
                if key(i) > key(max_value):
                    max_value = i
            return max_value
        else:
            for i in args:
                if i > max_value:
                    max_value = i
            return max_value
    else:
        rt = tuple(map(lambda x: x, *args))
        return sorted(rt, key=key)[-1]

def min(*args, **kwargs):
    key = kwargs.get('key')
    try:
        iterator = iter(args[0])
        if len(args) > 1:
            iterator2 = iter(args[0][0])
    except TypeError:
        min_value = args[0]
        if kwargs.get('key'):
            for i in args:
                if key(i) < key(min_value):
                    min_value = i
            return min_value
        else:
            for i in args:
                if i < min_value:
                    min_value = i
            return min_value
    else:
        rt = tuple(map(lambda x: x, *args))
        return sorted(rt, key=key)[0]
# test1 win out key
print(max([1, 2, 0, 3, 4]))
print(max(range(6)))
print(max((-9,)))
print(max([[1, 2], [7, 4], [5, 6]]))
print(max('hello'))
print(max(1, 4, 3))
print(max([1, 2, 3], [5, 6], [7], [0, 0, 0, 1]))

# test2 with key
print(max([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]))
print(max(2.2, 5.6, 5.9, key=int))
print(max(2.2, 2.3, -5.6, -5.9, key=int))

print(min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]))
print(min('hello'))
print(min((-9,)))
print(min(2.2, 5.6, 5.9, key=int))
print(min(2.2, 2.3, -5.6, -5.9, key=int))