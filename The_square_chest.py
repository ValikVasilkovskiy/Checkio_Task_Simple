# can be used for a matrix of length=16 element

def SortedByKey(data):
    return data[0]

def square_chest(lines_list:list):
    # sorted by first element in list
    lines_list.sort(key=SortedByKey)
    for i in range(len(lines_list)):
        s = sorted(lines_list[i])
        lines_list[i] = s
    lines_list.sort()
    square = 0
    # small square 1 x 1 lines
    for i in lines_list:
        next_range = lines_list[lines_list.index(i) + 1:]
        if [i[0], i[0]+4] in next_range:
            if [i[0]+4, i[0]+1+4] in next_range:
                if [i[0]+1, i[0]+1+4] in next_range:
                    square += 1
    # medium square 2 x 2 lines
    for i in lines_list:
        next_range = lines_list[lines_list.index(i) + 1:]
        if [i[0]+1, i[1]+1] in next_range:
            if [i[0], i[0]+4] in next_range:
                if [i[0]+4, i[0]+8] in next_range:
                    if [i[1]+1, i[1]+1+4] in next_range:
                        if [i[1]+1+4, i[1]+1+8] in next_range:
                            if [i[0]+8, i[1]+8] in next_range:
                                if [i[0]+1+8, i[1]+1+8] in next_range:
                                    square += 1
    # large square 3 x 3 lines
    for i in lines_list:
        next_range = lines_list[lines_list.index(i) + 1:]
        if [i[0]+1, i[1]+1] in next_range:
            if [i[0]+1+1, i[1]+1+1]in next_range:

                if [i[0], i[0]+4] in next_range:
                    if [i[0]+4, i[0]+8] in next_range:
                        if [i[0]+8, i[0]+12] in next_range:

                            if [i[1]+1+1, i[1]+1+1+4] in next_range:
                                if [i[1]+1+1+4, i[1]+1+1+8] in next_range:
                                    if [i[1]+1+1+8, i[1]+1+1+12] in next_range:

                                        if [i[0]+12, i[1]+12] in next_range:
                                            if [i[0]+1+12, i[1]+1+12] in next_range:
                                                if [i[0]+1+1+12, i[1]+1+1+12] in next_range:
                                                    square += 1
    return square
print(square_chest([[1,5],[5,9],[9,13],[13,14],[2,3],[4,8],[6,7],[6,10],[7,11],[10,14],[14,15],[16,15],[16,12],[8,12],[8,4],[10,11],[11,15]]))