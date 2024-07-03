# Exercise 1.3

## Learning Goals:

- Implement conditional statements in Python to determine program flow
- Use loops to reduce time and effort in Python programming
- Write functions to organize Python code

## Reflection Questions
1. In this Exercise, you learned how to use if-elif-else statements to run different tasks based on conditions that you define. Now practice that skill by writing a script for a simple travel app using an if-elif-else statement for the following situation:
- The script should ask the user where they want to travel.
- The user’s input should be checked for 3 different travel destinations that you define.
- If the user’s input is one of those 3 destinations, the following statement should be printed: “Enjoy your stay in ______!”
- If the user’s input is something other than the defined destinations, the following statement should be printed: “Oops, that destination is not currently available.

2. Imagine you’re at a job interview for a Python developer role. The interviewer says “Explain logical operators in Python”. Draft how you would respond

3. What are functions in Python? When and why are they useful?

4. In the section for Exercise 1 in this Learning Journal, you were asked in question 3 to set some goals for yourself while you complete this course. In preparation for your next mentor call, make some notes on how you’ve progressed towards your goals so far.

## Answers

1.
- destination = input("Where would you like to travel?")
- if destination == "Costa Rica":
    - print("Enjoy your stay in Costa Rica!")
- elif destination == "Mexico":
    - print("Enjoy your stay in Mexico!")
- elif destination == "Spain":
    - print("Enjoy your stay in Spain!")  
- else:
    - print("Oops, that destination is not currently available")

2. Logical operators in Python consist of and, not, and or, they are used in conditional statements.
   "And" checks if two different statements are true, if they both are it returns back true. If one or both is false then the statement returns false.
   "Or" checks if either of two statements are true, if one or both are true then it returns true. If both are false then it returns false.
   "Not" is the opposite of a conditional so if something is true then it will return false, and if something is false then it will return true.

3. Functions are a block of code that will be used multiple times within the same script file, this gets rid of redundant code and instead can just be called with the function name. This makes the code a lot easier to manage and makes it more reusable. They also create variables that are only able to be accessed inside of the function, as well as access variables that are outside the function.

4. I have been working with my private tutor to further understand the concept of object-oriented programming. Slowly I am getting the hang of it a little better. I have also been practicing writing code without referencing examples as much. I still have to reference examples but I am getting a little better at knowing at least part of it on my own without looking.
