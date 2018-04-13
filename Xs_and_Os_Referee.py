game_result = (["OO.","XOX","XOX"])
s = game_result
if (s[1][1] == s[0][0] == s[2][2] != '.') or (s[1][1] == s[0][2] == s[2][0] != '.'):
    print(s[1][1])
else:
    if s[0][0] == s[1][0] == s[2][0] != '.':
        print(s[0][0])
    elif s[0][1] == s[1][1] == s[2][1] != '.':
        print(s[0][1])
    elif s[0][2] == s[1][2] == s[2][2] != '.':
        print(s[0][2])
    else:
        if s[0][0] == s[0][1] == s[0][2] != '.':
            print(s[0][0])
        elif s[1][0] == s[1][1] == s[1][2] != '.':
            print(s[1][0])
        elif s[2][0] == s[2][1] == s[2][2] != '.':
            print(s[2][0])
        else:
            print('D')
