# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + "Pie")

# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)

# total_heights = 0
# for height in student_heights:
#     total_heights += height
# print(total_heights)

# number_of_students = 0
# for student in student_heights:
#     number_of_students += 1
# print(number_of_students)

# average_height = round(total_heights/number_of_students)
# print(average_height)

# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

# total = 0
# for number in range(2, 101, 2):
#     total += number
# print(total)

# total2 = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         total2 += number
# print(total2)

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)
print(number)

