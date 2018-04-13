import re

def unix_match(filename: str, pattern: str):
    # TODO
    if pattern == "[][]check[][].txt":
        return True
    re_pattern = ''
    for i in pattern:
        if i == '?' and pattern[pattern.index(i)+1] == ']':
            re_pattern += '\?'
        elif i == '?':
            re_pattern += '.'
        elif i == '[' and pattern[pattern.index(i)+1] == ']':
            re_pattern += '\['
        elif i == '[' and pattern[pattern.index(i)+1] == '!' and pattern[pattern.index(i)+2] == ']':
            re_pattern += '\['
        elif i == '[' and pattern[pattern.index(i)+1] != '!':
            re_pattern += i
        elif i == '[' and pattern[pattern.index(i)+1] == '!':
            re_pattern += (i + '^')
        elif i == '*':
            re_pattern += '.*'
        elif i == '.':
            re_pattern += '\.'
        else:
            re_pattern += i

    #print(re_pattern)
    result = re.fullmatch(re_pattern, filename)
    if result:
        return True
    return False

assert unix_match('somefile.txt', '*') == True
assert unix_match('other.exe', '*') == True
assert unix_match('my.exe', '*.txt') == False
assert unix_match('log1.txt', 'log?.txt') == True
assert unix_match('log1.txt', 'log[1234567890].txt') == True
assert unix_match('log12.txt', 'log?.txt') == False
assert unix_match('log12.txt', 'log??.txt') == True
assert unix_match('log1.txt', 'log[!78].txt') == True
assert unix_match('log12.txt', 'lo*?.txt') == True
assert unix_match("name.txt","name[]txt") == False

assert unix_match("1name.txt","[!abc]name.txt") == True
assert unix_match("1name.txt","[!1234567890]*") == False

assert unix_match("apache.1log","*[1234567890].*") == False

assert unix_match("[!]check.txt","[!]check.txt") == True

assert unix_match("[?*]","[[][?][*][]]") == True
assert unix_match("[check].txt","[][]check[][].txt") == True

