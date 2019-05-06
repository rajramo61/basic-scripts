def remove_spaces(str):
    if ' ' in str:
        temp = str.split(' ')
        return ''.join(temp)
    return str


def get_char_count(str):
    character_counter = {}
    for character in str[0:]:
        if character_counter.get(character) is None:
            character_counter[character] = 1
        else:
            character_counter[character] = character_counter.get(character) + 1
    return character_counter


def anagram_checker(str1, str2):
    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """

    # TODO: Write your solution here
    str1 = remove_spaces(str1).lower()
    str2 = remove_spaces(str2).lower()
    if len(str1) != len(str2):
        return False
    character_counter1 = get_char_count(str1)
    character_counter2 = get_char_count(str2)
    if character_counter1 == character_counter2:
        return True
    else:
        return False


print("Pass" if not (anagram_checker('water', 'waiter')) else "Fail")
print("Pass" if anagram_checker('Dormitory', 'Dirty room') else "Fail")
print("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
print("Pass" if not (anagram_checker('A gentleman', 'Elegant men')) else "Fail")
print("Pass" if anagram_checker('Time and tide wait for no man', 'Notified madman into water') else "Fail")