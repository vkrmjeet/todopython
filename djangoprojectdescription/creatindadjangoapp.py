'''
     to create a django app we have to use the command
         django-admin startapp jobs (this will create some files inside the directory)
     by convention app names are plural.
     avoid using app names that can conflict with built in python or django packages
          or functions.
    use the same directory which have manage.py file.

    to activate app we need to make django aware about the app and add it to the
    list of installed files in the settings.py file.
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todolist',(this is the file mentioned in settings.py
    in order to make the project aware)
]


'''