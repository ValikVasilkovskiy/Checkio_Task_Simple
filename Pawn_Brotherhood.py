pawns = ({"b4", "c4", "d4", "e4", "f4", "g4", "e5"})
game_field = [[0 for rows in range(8)] for columns in range(8)]
location = []
safe_count = 0
for data in pawns:
    if 'b' in data:
        location.append('2' + data[1])
    elif 'a' in data:
        location.append('1' + data[1])
    elif 'c' in data:
        location.append('3' + data[1])
    elif 'd' in data:
        location.append('4' + data[1])
    elif 'e' in data:
        location.append('5' + data[1])
    elif 'f' in data:
        location.append('6' + data[1])
    elif 'g' in data:
        location.append('7' + data[1])
    elif 'h' in data:
        location.append('8' + data[1])
print(location)
for values in location:
    game_field[-int(values[1])][int(values[0])-1] = 1
for v in game_field:
    print(v)
for i in range(len(game_field) -1):
    for j in range(1, len(game_field[i]) -1):
        if game_field[i][j] == 1:
            if game_field[i+1][j-1] == 1 or game_field[i+1][j+1] == 1:
                safe_count += 1
for i in range(1, len(game_field) -1):
    if game_field[i][0] == 1:
        if game_field[i+1][1] == 1:
            safe_count += 1
for i in range(1, len(game_field) -1):
    if game_field[i][-1] == 1:
        if game_field[i+1][-2] == 1:
            safe_count += 1
print(safe_count)




