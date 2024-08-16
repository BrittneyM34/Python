# Exercise 2.8

## Learning Goals:

- Enhance user experience and look and feel of your web application using CSS and JS
- Deploy your Django web application on a web server
- Curate project deliverables for your portfolio

## Reflection Questions: 

1. Explain how you can use CSS and JavaScript in your Django web application

2. In your own words, explain the steps you'd need to take to deploy your Django web application

3. You've now finished Achievement 2 and, with it, the whole course! Take a moment to relect on your learning:
   a. What went well during this Achievement?
   b. What's something you're proud of?
   c. What was the most challenging aspect of this Achievement?
   d. Did this Achievement meet your expectations? Did it give you the confidence to start working with your new Django skills?
   
## Answers:
1. Place the static files and a static directory within the app and use
   {% load static %}
   <link rel="stylesheet" type="text/css" href="{% static 'css/style.css'%}">
   <script scr="{% static 'js/script.js' %}"></script>

2. To deploy a Django web application, the first thing you need to do is set up a production server. Next, configure settings for production, such as setting debug to False and configuring a production database. Finally, push the code to the server and run the commands necessarty to apply the migrations and collect static files.

3. I think mostly my troubleshooting went well. For the most part I was able to figure out the issues with my code on my own by searching online using the error messages. I am proud that I was able to build a fully functioning recipe app. I think my interface looks decent for what skills I have. The most challenging aspect was working with Heroku. For some reasons I always have issues with Heroku and deploying my app. This achievement gave me a basic kownledge and set of skills that I can use to dive deeper into my knowledge of Python and Django. It has given me confidence that I am able to complete tasks.
