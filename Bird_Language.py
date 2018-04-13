"""
Input: A bird phrase as a string.
Output: The translation as a string.
Example:
translate("hieeelalaooo") == "hello"
"""

def translate(phrase):
    vowels = "aeiouy"
    stack, str_translate = [], ''
    for i in phrase: stack.append(i)
    # create string as h0e00l0l0o00
    for i in range(len(stack)):
        if str(stack[i]).isalpha():
            if stack[i] in vowels:
                stack[i+1] = 0
                stack[i+2] = 0
            else:
                stack[i+1] = 0
    # del 0 and create result
    for i in stack:
        if i != 0 or i == ' ':
            str_translate += str(i)
    return str_translate

#test
print(translate("sooooso aaaaaaaaa"))
