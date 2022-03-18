'''
    we can run our project with the help of django development server.
      the command is : python manage.py runserver
      by default the development server uses the port 8000.
      we can change is by using
       python manage.py runserver 8080
      if we don't specify any port it automatically selects the port.
(todolist) E:\courses\python\djangoproject\todolist>python manage.py runserver 8080
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
March 12, 2022 - 06:59:58
Django version 4.0.3, using settings 'mylist.settings'
Starting development server at http://127.0.0.1:8080/
Quit the server with CTRL-BREAK.



to stop development server just type ctrl+c
'''