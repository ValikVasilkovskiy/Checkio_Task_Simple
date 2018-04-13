# function find palindromic in data
def is_palindromic(data):
    for i in range(int(len(data)/2)):
        if data[i] != data[-(i + 1)]:
            return False
    return True
# sort by length of string
def sort_by_len(string):
    return len(string)
def longest_palindromic(text):
    stack = []
    if is_palindromic(text):
        return text
    else:
        for i in range(len(text)):
            for j in range(-1, (-len(text)) + i, -1):
                if text[i] == text[j]:
                    if is_palindromic(text[i:j+1]):
                        stack.append(text[i:j+1])
    stack.sort(key=sort_by_len)
    if not stack:
        return text[0]
    longest = str(stack[0])
    for i in stack:
        if len(i) > len(longest):
            longest = i
    return longest
print(longest_palindromic("ab"))