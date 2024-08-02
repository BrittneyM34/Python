# Exercise 2.4

## Learning Goals:

- Summarize the process of creating views, templates, and URLs
- Explain how the "V" and "T" parts of MVT architecture work
- Create a frontend page for your web application

## Reflection Questions: 

1. Do some research on Django views. In your own words, use an example to explain how Djano views work

2. Imagine you're working on a Django web development project, and you anticipate that you'll have to reuse lots of code in various parts of the project. In this scenario, you will use Djanog function based views or class based views, and why?

3. Read Django's documentation on the Django template language and make some notes on its basics

## Answers:
1. In Django the views are Python functions that handle requests and return web responses. They are used like a bridge between the user and the data processed by the application.

2. I would use class based views because they are easier to reuse and they will keep the code more organized.

3. Django's template language is designed to be simple and intuitive. This allows you to separate the presentation logic from the application code.
Some basic syntax:
<h1>Hello, {{ name }}!</h1>
{# This is a comment #}
{% if user.is_authenticated %}
  Welcome, {{ user.username }}!
{% else %}
  Please log in.
{% endif %}
