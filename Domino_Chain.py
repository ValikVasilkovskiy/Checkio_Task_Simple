import itertools

def domino_chain(tiles: str):
    list_stack = []
    temp_stack = []
    for i in tiles:
        if i.isdigit():
            temp_stack.append(int(i))
            if len(temp_stack) == 2:
                list_stack.append(temp_stack)
                if list(reversed(temp_stack)) not in list_stack:
                    list_stack.append(list(reversed(temp_stack)))
                temp_stack = []

    tuple_stack = tuple(map(lambda x: tuple(x), list_stack))
    len_block_tiles = len(tiles.split(','))
    combinations = set(itertools.permutations(tuple_stack, len_block_tiles))

    print(len(combinations))

    domino_combinations = []
    for i in combinations:
        for j in range(len(i)-1):
            if i[j][1] != i[j+1][0]:
                break
        else:
            for part_tuple_stack in tuple_stack:
                if part_tuple_stack not in i and tuple(reversed(part_tuple_stack)) not in i:
                    break
            else:
                if i not in domino_combinations and tuple(reversed(tuple(map(lambda x: tuple(reversed(x)),i)))) not in domino_combinations:
                    domino_combinations.append(i)

    return len(domino_combinations)

# test
print(domino_chain("0-2, 0-5, 1-5, 1-3, 5-5")) # return 1 combination
#print(domino_chain("1-5, 2-5, 3-5, 4-5, 3-4")) # return 2 combination
#print(domino_chain("0-5, 1-5, 2-5, 3-5, 4-5, 3-4")) # return 0 combination
#print(domino_chain("0-1, 0-2, 1-3, 1-2, 3-4, 2-4")) # 6
#print(domino_chain("0-1, 0-2, 1-3, 1-2, 3-4, 2-4, 3-0, 0-4")) # 0
#print(domino_chain("1-2, 2-2, 2-3, 3-3, 3-1")) # 5
#print(domino_chain("1-4, 3-4, 0-4, 0-5, 4-5, 2-4, 2-5")) # 0
#print(domino_chain("1-4, 1-5, 0-2, 1-6, 4-6, 4-5, 5-6")) # 0
#print(domino_chain("1-2, 2-3, 2-4, 3-4, 2-5, 2-6, 5-6")) # 8
#print(domino_chain("1-2, 2-3, 3-1, 4-5, 5-6, 6-4")) # 0
#print(domino_chain("1-2, 1-4, 1-5, 1-6, 1-1, 2-5, 4-6")) # 28


