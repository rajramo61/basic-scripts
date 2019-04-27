lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    counter = 0
    # Implement your generator function here
    while counter < len(iterable):
        yield start + counter, iterable[counter]
        counter += 1

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))
