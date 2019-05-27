"""
Problem Statement:
A child is running up a staircase with and can hop either 1 step, 2 steps or 3 steps at a time.
If the staircase has n steps, write a function to count the number of possible ways in which child
can run up the stairs.

For e.g.

n == 1 then answer = 1

n == 3 then answer = 4

n == 5 then answer = 13
"""


def staircase_lazy(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    return staircase_lazy(n - 1) + staircase_lazy(n - 2) + staircase_lazy(n - 3)


def staircase(n):
    tracker = {}
    return staircase_quick(n, tracker)


def staircase_quick(n, tracker):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        if n-1 in tracker:
            output_one = tracker.get(n-1)
        else:
            output_one = staircase_quick(n-1, tracker)
        if n-2 in tracker:
            output_two = tracker.get(n-2)
        else:
            output_two = staircase_quick(n-2, tracker)
        if n - 3 in tracker:
            output_three = tracker.get(n - 3)
        else:
            output_three = staircase_quick(n - 3, tracker)

        output = output_one + output_two + output_three
        tracker[n] = output
    return output


def test_function(test_case):
    answer = staircase(test_case[0])
    if answer == test_case[1]:
        print("Pass")
    else:
        print("Fail")


test_case = [4, 7]
test_function(test_case)

test_case = [5, 13]
test_function(test_case)

test_case = [20, 121415]
test_function(test_case)
