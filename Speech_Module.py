def speech_module(number):
    dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
            10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
            17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    dict_sec = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
                90: 'ninety'}
    string_data, speech = str(number), ''
    if number in dict:
        speech = dict[number]
    elif number in dict_sec:
        speech = dict_sec[number]
    elif len(str(number)) == 2:
        # first number * 10 = in dict_dec (ex: 2 * 10 = twenty)
        speech = dict_sec[int(string_data[0])*10] + ' ' + dict[int(string_data[1])]
    elif len(str(number)) == 3:
        # middle number = 0 bun not 100 (example: 101)
        if int(string_data[1]) == 0 and number % 100 != 0:
            speech = dict[int(string_data[0])] + ' hundred ' + dict[int(string_data[2])]
        # two last number in dict (example: 112)
        elif int(string_data[1] + string_data[2]) in dict:
            speech = dict[int(string_data[0])] + ' hundred ' + dict[int(string_data[1] + string_data[2])]
        # two last number in dict_sec (example: 420)
        elif int(string_data[1] + string_data[2]) in dict_sec:
            speech = dict[int(string_data[0])] + ' hundred ' +  dict_sec[int(string_data[1] + string_data[2])]
        # hundred (example: 100, 200)
        elif number % 100 == 0:
            speech = dict[int(string_data[0])] + ' hundred'
        # all other number (example: 432) str(4 + (3*10) * 2)
        else:
            speech = dict[int(string_data[0])] + ' hundred ' + dict_sec[int(string_data[1])*10] + ' ' + dict[int(string_data[2])]
    return speech
print(speech_module(909))