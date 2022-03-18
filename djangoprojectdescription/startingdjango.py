''''
   Microsoft Windows [Version 10.0.19042.1466]
(c) Microsoft Corporation. All rights reserved.

C:\Users\bobyt>cd /d E:

E:\>cd E:\courses\python\djangoproject

E:\courses\python\djangoproject>virtalenv todolist
'virtalenv' is not recognized as an internal or external command,
operable program or batch file.

E:\courses\python\djangoproject>pip install virtualenv
Collecting virtualenv
  Downloading virtualenv-20.13.3-py2.py3-none-any.whl (8.7 MB)
     |████████████████████████████████| 8.7 MB 437 kB/s
Collecting distlib<1,>=0.3.1
  Using cached distlib-0.3.4-py2.py3-none-any.whl (461 kB)
Requirement already satisfied: six<2,>=1.9.0 in c:\users\bobyt\miniconda3\lib\site-packages (from virtualenv) (1.16.0)
Collecting filelock<4,>=3.2
  Using cached filelock-3.6.0-py3-none-any.whl (10.0 kB)
Collecting platformdirs<3,>=2
  Using cached platformdirs-2.5.1-py3-none-any.whl (14 kB)
Installing collected packages: platformdirs, filelock, distlib, virtualenv
Successfully installed distlib-0.3.4 filelock-3.6.0 platformdirs-2.5.1 virtualenv-20.13.3

E:\courses\python\djangoproject>virtualenv todolist
created virtual environment CPython3.9.7.final.0-64 in 5707ms
  creator CPython3Windows(dest=E:\courses\python\djangoproject\todolist, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\bobyt\AppData\Local\pypa\virtualenv)
    added seed packages: pip==22.0.4, setuptools==60.9.3, wheel==0.37.1
  activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

E:\courses\python\djangoproject>todolist/scripts/activate
'todolist' is not recognized as an internal or external command,
operable program or batch file.

E:\courses\python\djangoproject>todolist\scripts\activate

(todolist) E:\courses\python\djangoproject>django-admin startproject todolist
'django-admin' is not recognized as an internal or external command,
operable program or batch file.

(todolist) E:\courses\python\djangoproject>pip install django
Collecting django
  Using cached Django-4.0.3-py3-none-any.whl (8.0 MB)
Collecting asgiref<4,>=3.4.1
  Using cached asgiref-3.5.0-py3-none-any.whl (22 kB)
Collecting tzdata
  Using cached tzdata-2021.5-py2.py3-none-any.whl (339 kB)
Collecting sqlparse>=0.2.2
  Using cached sqlparse-0.4.2-py3-none-any.whl (42 kB)
Installing collected packages: tzdata, sqlparse, asgiref, django
Successfully installed asgiref-3.5.0 django-4.0.3 sqlparse-0.4.2 tzdata-2021.5

(todolist) E:\courses\python\djangoproject>django-admin startproject todolist
CommandError: 'E:\courses\python\djangoproject\todolist' already exists

(todolist) E:\courses\python\djangoproject>cd E:\courses\python\djangoproject\todolist

(todolist) E:\courses\python\djangoproject\todolist>django-admin staartproject todolist
No Django settings specified.
Unknown command: 'staartproject'. Did you mean startproject?
Type 'django-admin help' for usage.

(todolist) E:\courses\python\djangoproject\todolist>django-admin startproject todolist

(todolist) E:\courses\python\djangoproject\todolist>
   '''