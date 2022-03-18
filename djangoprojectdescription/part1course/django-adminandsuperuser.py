'''
     django admin and superuser
        django comes with a built in administrative interface page.
        django superuser is used to manage the django admin page.
     to create a superuser account
         python manage.py createsuperuser
         (todolist) E:\courses\python\djangoproject\todolist>python manage.py createsuperuser
                Username (leave blank to use 'bobyt'): admin
                Email address: bobythakran@gmail.com
                Password:admin
                Password (again):admin
                The password is too similar to the username.
                This password is too short. It must contain at least 8 characters.
                This password is too common.
                Bypass password validation and create user anyway? [y/N]: y
                Superuser created successfully.

         check the user by starting the server
         python manage.py runserver

         you can go to the admin panel by visiting the link
               http://127.0.0.1:8000/admin/
'''