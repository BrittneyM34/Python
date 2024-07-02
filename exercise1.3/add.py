# a = int(input("Enter a number: "))
# b = int(input("Enter another number to be added to the first: "))
# print("The sum of these numbers is " + str(a + b))

# age = int(input("Enter your age: "))
# print("Age between 18 and 35: " + str(18 < age < 35)) 

# number = 5

# while number < 11:
#     print(number)
#     number += 1

num = int(input("Enter a number to be divided: "))
start = int(input("Enter a starting point for the divisor: "))
end = int(input("Enter an end point for the divisor: "))

for div in range(start, end):
    if div == 0:
        print("Division by zero, exiting")
        continue
    print(num / div)