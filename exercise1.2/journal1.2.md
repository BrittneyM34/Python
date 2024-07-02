# Exercise 1.2

## Learning Goals:

- Explain variables and data types in Python
- Summarize the use of objects in Python
- Create a data structure for your Recipe app
  
## Reflection Questions 

1. Imagine you’re having a conversation with a future colleague about whether to use the iPython Shell instead of Python’s default shell. What reasons would you give to explain the benefits of using the iPython Shell over the default one

2. Python has a host of different data types that allow you to store and organize information. List 4 examples of data types that Python recognizes, briefly define them, and indicate whether they are scalar or non-scalar.

3. A frequent question at job interviews for Python developers is: what is the difference between lists and tuples in Python? Write down how you would respond.

4. In the task for this Exercise, you decided what you thought was the most suitable data structure for storing all the information for a recipe. Now, imagine you’re creating a language-learning app that helps users memorize vocabulary through flashcards. Users can input vocabulary words, definitions, and their category (noun, verb, etc.) into the flashcards. They can then quiz themselves by flipping through the flashcards. Think about the necessary data types and what would be the most suitable data structure for this language-learning app. Between tuples, lists, and dictionaries, which would you choose? Think about their respective advantages and limitations, and where flexibility might be useful if you were to continue developing the language-learning app beyond vocabulary memorization.

## Answers:

1. One of the benefits of the iPython shell is it has an auto tab function. Instead of typing out long variables or function names you can just start typing it and his tab and it will suggest what to finish typing. It also provides different colors and will indent code as needed, making it easier to read and understand. It also can automatically reload your code when you save the file instead of having to restart the entire shell.

2.
    ### Tuples
    A tuple is an ordered collection of elements. It is similar to a list, the difference is that tuples can not be modified once they are created. They are non-scalar.

    ### Floats
    A float represents numbers with decimal points. They are scalar

    ### List
    A list is an ordered collection of items that can hold different types of data. It is non-scalar

    ### Dictionary 
    Dictionaries are collections of key-value pairs and they must be unique. The values can be any data type. They are non-scalar

3. Lists are more versatile and they can be modified after they are created. Elements can be added or removed using methods. They are useful for dynamic data that needs updated often. Tuples can not be changed once they are created. This ensures data integrity and are more useful for situations where the data should not be modified.

4. To store information in flash cards for a language learning app I would store all of the vocabulary words into lists. Lists are easy to add, remove, or change data so the user can easily add or remove words as needed. They also maintain the order that the information is added, so users can see the words in a specific sequence that they choose. I would add these lists into dictionaries so I am able to store all of the other information like definitions and categories. Dictionaries also provide flexibility in editing data so the user can change defintions and other information.
