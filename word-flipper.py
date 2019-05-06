def reverse_word(word):
    length = len(word)
    flip_word = ''
    for index in range(len(word)):
        flip_word += word[length - index - 1]
    return flip_word


def word_flipper(our_string):
    """
    Flip the individual words in a sentence

    Args:
       our_string(string): String with words to flip
    Returns:
       string: String with words flipped
    """

    # TODO: Write your solution here
    sentence = []
    if ' ' in our_string:
        words = our_string.split(' ')
        for word in words:
            sentence.append(reverse_word(word))
        return ' '.join(sentence)
    else:
        return reverse_word(our_string)


def word_flipper_class(our_string):

    """
    Flip the individual words in a sentence

    Args:
       our_string(string): Strings to have individual words flip
    Returns:
       string: String with words flipped
    """

    word_list = our_string.split(" ")

    for idx in range(len(word_list)):
        word_list[idx] = word_list[idx][::-1]

    return " ".join(word_list)


print("Pass" if ('retaw' == word_flipper('water')) else "Fail")
print("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
print("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")