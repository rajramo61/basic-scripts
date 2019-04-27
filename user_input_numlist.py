# initiate empty list to hold user input and sum value of zero
user_list = [23, 24, 25, 26, 27, 28, 29, 30, 31, 22]
list_sum = 0

# seek user input for ten numbers
for i in range(10):
    userInput = eval(input("Enter any 2-digit number: "))

# check to see if number is even and if yes, add to list_sum
# print incorrect value warning  when ValueError exception occurs
    try:
        number = userInput
        user_list.append(number)
        if number % 2 == 0:
            list_sum += number
    except ValueError:
        print("Incorrect value. That's not an int!")

print("user_list: {}".format(user_list))
print("The sum of the even numbers in user_list is: {}.".format(list_sum))
