# Exercise 2.3

## Learning Goals:

- Discuss Django models, the "M" part of Django's MVT architecture
- Create apps and models representing different parts of your web application
- Write and run automated tests

## Reflection Questions: 

1. Do some research of Django models. In your own words, write down how Django models work and what their benefits are

2. In your own words, explain why it is crucial to write test cases from the beginning of a project. You can take an example project to explain your answer

## Answers:
1. Django is like the backbone of an application. It uses models which basically are Python classes that define the structure of the database tables. It makes it easier to interact with and manage the data. It also enforces data integrity so the data is not lost or accidentally changed.

2. It is important to write test cases from the beginning because it makes it easier to spot errors if you are able to fix them from the start. If you wait until you have many models and apps, it is going to be a tough time figuring out exactly where your errors are. But if you start from the beginning then little by little you can fix your errors as you go so things do not get very messed up by the end. It also forces you to think of potential issues up front to proactively try to avoid any issues that may arise during the development, as well as it helps you write cleaner and more testable code.
