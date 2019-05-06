# Code


def string_reverser(our_string):
    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """

    # TODO: Write your solution here
    str_list = list(our_string)
    last_index = len(str_list) - 1
    mid_length = int(len(str_list)/2)
    for index, val in enumerate(str_list):
        if index < mid_length:
            temp = str_list[index]
            str_list[index] = str_list[last_index - index]
            str_list[last_index - index] = temp
    return ''.join(str_list)


def string_reverser_class(our_string):
    new_string = ""

    # Iterate over old string
    for i in range(len(our_string)):
        # Grab the charecter from the back of the string and add them to the new string
        new_string += our_string[(len(our_string)-1)-i]

    # Return our solution
    return new_string


print ("Pass" if ('retaw' == string_reverser('water')) else "Fail")
print ("Pass" if ('!noitalupinam gnirts gnicitcarP' == string_reverser('Practicing string manipulation!')) else "Fail")
print ("Pass" if ('3432 :si edoc esuoh ehT' == string_reverser('The house code is: 2343')) else "Fail")