def get_remender(first, second):
    remender = first % second
    if remender == 0:
        return second
    else:
        return get_remender(second, remender)

value = get_remender(1344, 217)
print(value)
