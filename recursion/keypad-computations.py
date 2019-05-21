def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""


def keypad(num):
    '''
    :param num: string
    :return: list of strings with all possible combinations
    '''
    result = []
    string = ""

    keypad_helper(num, string, result)
    return result


def keypad_helper(num, string, result):
    if len(num) == len(string):
        result.append(string)
        return

    for character in get_characters(int(num[len(string)])):
        string += character
        keypad_helper(num, string, result)
        string = string[:-1]


def keypad_class(num):
    '''
    :param num: int
    :return: list of strings with all possible combinations
    '''
    # Come back again
    if num <= 1:
        return [""]
    elif 1 < num <= 9:
        return list(get_characters(num))

    last_digit = num % 10
    small_output = keypad(num//10)
    keypad_string = get_characters(last_digit)
    output = list()
    for character in keypad_string:
        for item in small_output:
            new_item = item + character
            output.append(new_item)
    return output
    pass


print(keypad('2359'))


