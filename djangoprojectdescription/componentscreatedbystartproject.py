'''
    startproject creates some directories automatically
               which are required for it to function.
        _init_.py : this is created to tell python that this directory is an
             empty python package.
        settings.py : this is used to change the setting of our project.
           ex : change of database or change of timezone.
        urls.py : this is an entry point or url declaration for our django project.
            urlpatterns are used for storing address.
            it stores a list of patter for reserver that is like a postman which
            checks if the path really exist when a request is made.
        wsgi.py : django comes with a default development server that
           lets us check our project and helps us to run it but it cannot be
           used for deployment. this file is required for deployment of the project.
        manage.py : this exists in the root folder.
           it is a command line utility that lets you interact with the project.
           it is very important.
           all the commands are run through manage.py file.
        
'''