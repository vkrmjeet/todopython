'''
    after going in the needed directory run the command
        django-admin startproject project_name
           or
        django-admin startproject project_name .
   the difference is outer folder and inner folder is created with the same name.
      project_name>project_name>files
    if period is used outer folder is not created.


   avoid naming projects after built in python or django components
   example: django or test . which conflicts with built in python package.

   .tells the script to install django in your current directory . this avoids
   the creation of an extra outer directory with the same name as the project
   directory. this can be renamed if created.
'''