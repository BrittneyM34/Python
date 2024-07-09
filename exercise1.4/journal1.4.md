# Exercise 1.4

## Learning Goals:
- Use files to store and retrieve data in Python

## Reflection Questions

1. Why is file storage important when you’re using Python? What would happen if you didn’t store local files?

2. In this Exercise you learned about the pickling process with the pickle.dump() method. What are pickles? In which situations would you choose to use pickles and why?

3. In Python, what function do you use to find out which directory you’re currently in? What if you wanted to change your current working directory?

4. Imagine you’re working on a Python script and are worried there may be an error in a block of code. How would you approach the situation to prevent the entire script from terminating due to an error?

5. You’re now more than halfway through Achievement 1! Take a moment to reflect on your learning in the course so far. How is it going? What’s something you’re proud of so far? Is there something you’re struggling with? What do you need more practice with? Feel free to use these notes to guide your next mentor call.
   
## Answers
1. File storage is important because when you are using data in a script that will need to be accessed multiple times, the data in erased once the file is closed. By using a file to store the data that will need to be accessed more than once can help prevent data loss.

2. Pickles convert an object into a byte stream so it can be stored. They are useful for writing to and reading external files that consist of data structures.

3. The function that is used for finding out which directory you're in is os.getcwd(). To change the directory it would be os.chdir().

4. A way to approach the situation is to you try, except, else, finally blocks. The "try" is used to attempt to execute a block of code that may result in an error. The "except is used to account for any type of error that the user may encounter while running the code. The "finally" is used to continue the code in the block even if an error has appeared before it. "Else" is used to run more code if the "try" block completed successfully without any errors.

5. I am having some trouble understanding the pickles. I understand it converts the data but I guess I don't really understand much more than that, but I do plan on looking into pickles a bit more to understand them a bit better. When I see the code in front of me it makes sense in my head how it works, but I am still having trouble getting started on things on my own without referencing examples. 
