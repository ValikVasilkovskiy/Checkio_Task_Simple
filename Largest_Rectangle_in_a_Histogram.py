def number(data):
    temp_stack = []
    for i in range(1, data + 1): temp_stack.append(i)
    return temp_stack

def largest_histogram(histogram):
    stack, main_stack = [], []
    if len(histogram) == 1:
        return histogram[-1]
    # create view histogram
    #for i in histogram: stack.append(number(i))
    # for all [i][j] in stack, start with j = -1
    for i in histogram:
        # reversed stack[i]
        for j in reversed(number(i)):
            point_down = 1
            start_point = histogram.index(i) + 1
            for r in histogram[start_point:]:
                if j in number(r):
                    point_down += 1
                    if main_stack == []:
                        main_stack.append(point_down * j)
                    else:
                        if (point_down * j) > main_stack[-1]:
                            main_stack = []
                            main_stack.append(point_down * j)
                else:
                    point_down = 1
                    #main_stack.append(point_down * stack[i][j])
                    break

    #main_stack.sort()
    return main_stack[-1]




