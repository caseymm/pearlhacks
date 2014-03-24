#Culture of Yes (tentative)

##Postgres
This is currently set up to run off of postgres. To get this to work: 
- make sure that you have postgres and (I use) pgAdmin installed
- make sure to edit the database settings in your settings.py file (you may also enable the commented out sqlite there if you so wish)

##Data info
Most of the current data is located in colleges_clean.json. Run:
$ python manage.py loaddata colleges_clean.json

##Run Scrapers
All of the scrapers are run as management commands. From home project directory, you run:
$ python manage.py [filename] 
- do not include the .py on the filename
- ex) python manage.py north_carolina   