WhatsForDinner

This Django web page is a simple implementation of a calendar to help you organize your dinners. 

Cant decide what to have? Roll the dice to pull in a random food graciously provided by random-data-api.com!

Currently running the webserver using the built-in Django Runserver, with future planning to implement a dockerized container alongside nginx and gunicorn

Getting started is as simple as cloning the repo into VS code, and hitting F5. The sqlite3 db is supplied within the repo for general testing 

Login is admin
password is admin

Walkthrough
1. Clone the repo
2. Start the django runserver.py
3. Navigate to the localhost on port 8080
4. Login using admin
5. Click on a date on the calendar to edit or view the dinner if there is already one selected
6. Roll the dice for a new random dinner that will get saved into your invetory once you lock it in, or select from an existing dish you've previously had!
7. Manage your existing dinner ideas from the left menu, which will allow you to search and edit existing ideas, or create new ones.
8. Admin site is available aswell which you can get to by navigating to the top right and clicking on your profile

Full disclosure, the model of the dinner was modeled after the data sent by the API. So plans to look for a "Random Recipe" API is in the works

Future plans include:
-Images of the meals
-Tweaking the recipe model by adding more relevant fields (API was limited to the data i could get)
-Dynamic portions on ingredients
-Grocery list export
-Import standard recepie format from websites
-Add ability to do lunch and breakfast (maybe?.. the name would have to change i guess)
-Dockerizing the site

Criticism welcome!
