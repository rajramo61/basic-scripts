# a is sorted list
def binary_search(a, key):
    # TODO: Write - Your - Code
    length = len(a)
    if a is None or length == 0:
        return -1

    mid = length // 2
    if a[mid] == key:
        return mid

    elif a[mid] > key:
        return search(a, 0, mid - 1, key)
    else:
        return search(a, mid + 1, length, key)


def search(a, start, end, key):
    if start > end:
        return -1
    mid = start + (end - start) // 2
    if a[mid] == key:
        return mid
    else:
        if a[mid] > key:
            return search(a, 0, mid - 1, key)
        else:
            return search(a, mid + 1,  end, key)


print(binary_search([2, 3, 4, 5, 6, 7, 9, 10], 9))
print(binary_search([2, 3, 4, 5, 6, 7, 9, 10], 4))
print(binary_search([2, 3, 4, 5, 6, 7, 9, 10], 0))
