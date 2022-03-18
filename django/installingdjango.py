'''
     make sure you are in correct directory
         we can use command line : pip install django
         we can also use by creating a requirement text file and putting it in the root of our directory.
              requirement.txt : Django~=2.0.6 (this should be written on the first line of requirement.txt file)
                   this should be used if specific version of django is required.
                   and then we have to run the command : pip install -r requirement.txt

         we can also use the command directly to install the latest version.

(todolist) E:\courses\python\django>pip install django
Collecting django
  Downloading Django-4.0.3-py3-none-any.whl (8.0 MB)
     ---------------------- 8.0/8.0 MB 1.6 MB/s eta 0:00:00
Collecting asgiref<4,>=3.4.1
  Downloading asgiref-3.5.0-py3-none-any.whl (22 kB)
Collecting tzdata
  Downloading tzdata-2021.5-py2.py3-none-any.whl (339 kB)
     ------------------ 339.4/339.4 KB 1.2 MB/s eta 0:00:00
Collecting sqlparse>=0.2.2
  Downloading sqlparse-0.4.2-py3-none-any.whl (42 kB)
     --------------------------- 42.3/42.3 KB ? eta 0:00:00
Installing collected packages: tzdata, sqlparse, asgiref, django
Successfully installed asgiref-3.5.0 django-4.0.3 sqlparse-0.4.2 tzdata-2021.5
WARNING: You are using pip version 22.0.3; however, version 22.0.4 is available.
You should consider upgrading via the 'E:\courses\python\django\todolist\Scripts\python.exe -m pip install --upgrade pip' command.

(todolist) E:\courses\python\django>

to check the version of django instaled into oyr machine we can use the command
python -m django --version
(todolist) E:\courses\python\django>python -m django --version
4.0.3


'''