# Exercise 2.6

## Learning Goals:

- Create authentication for your web application
- use GET and POST methods
- Password protect your web application's views

## Reflection Questions: 

1. In your own words, write down the importance of incorporating authentication into an application. You can take an example application to explain your answer

2. In your own words, explain the steps you should take to create a login for you Django web aplication

3. Look up the following three Django functions on Django's official documentation and/or other trusted sources and write a brief description of each
   authenticate()
   redirect()
   include()
   
## Answers:
1. The importance of incorporating authentication has many uses. It allows the developer to be in control of what the customer can see versus an employee. This way it protects personal information of the company as well as the users. It protects sensitive data from users who may not be authorized to see it

2. To create a login you need to set up the authentication system by adding 'django.contrib.auth' to the INSTALLED_APPS list in the settings.py file. Then, you have to create a login and logout view, register and map out the URLs, require authentication to view, and create the html files for the views of each page.

3.
  authenticate(): Takes the user credentials as parameters and validates it. If it is valid then it will return the user object, if not it will return 'none'
   redirect(): It takes the URL of a page to direct the user to. Then it returns the view of the page and displays the template to the browser
   include(): It adds URLs from the apps directory to the urls.py file in the main project directory
