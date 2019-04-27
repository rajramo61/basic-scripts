def get_user_input():
    my_map = {}
    with open('flower.txt') as file:
        for line in file:
            key, value = line.split(': ')
            my_map[key.upper()] = value
    return my_map


def main():
    my_map = get_user_input()
    user_name = input('Enter your First [space] Last name only:')
    print("Unique flower name with the first letter: {}".format(my_map.get(user_name[0])))


main()
