'''
     we will be scrapping
        :- https://bluelimelearning.github.io/my-fav-quotes/
     virtual environment
        it is isolated python environment
        allows you to use different packages and versions for various prokects.
        virtualenv is the tool used to create a virtual environment.
    let us create a new directory and create a virtual environment in it.
    to change directory in command prompt use
    cd /d E: (drive name) and then directories within the drive

    C:\Users\bobyt>cd /d E:

E:\>cd E:\courses\python\webscrapingwithpython\webscraping

E:\courses\python\webscrapingwithpython\webscraping>pip install virtualenv



Creating an isolated virtual environment
   make sure you are in your project directory
   virtualenv myenv
E:\courses\python\webscrapingwithpython\webscraping>virtualenv myenv
created virtual environment CPython3.10.0.final.0-64 in 5760ms
  creator CPython3Windows(dest=E:\courses\python\webscrapingwithpython\webscraping\myenv, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\bobyt\AppData\Local\pypa\virtualenv)
    added seed packages: pip==22.0.3, setuptools==60.9.3, wheel==0.37.1
  activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator



ACtivating virtual environment
E:\courses\python\webscrapingwithpython\webscraping>myenv\scripts\activate

(myenv) E:\courses\python\webscrapingwithpython\webscraping>

Deactivate virtual environment :- myenv\scripts\deactivate



Installing Beautifulsoup(gitbash terminal can also be used to install this)
(myenv) E:\courses\python\webscrapingwithpython\webscraping>pip install bs4
Collecting bs4
  Downloading bs4-0.0.1.tar.gz (1.1 kB)
  Preparing metadata (setup.py) ... done
Collecting beautifulsoup4
  Downloading beautifulsoup4-4.10.0-py3-none-any.whl (97 kB)
     ---------------------------------------- 97.4/97.4 KB 253.4 kB/s eta 0:00:00
Collecting soupsieve>1.2
  Downloading soupsieve-2.3.1-py3-none-any.whl (37 kB)
Building wheels for collected packages: bs4
  Building wheel for bs4 (setup.py) ... done
  Created wheel for bs4: filename=bs4-0.0.1-py3-none-any.whl size=1272 sha256=10ea79a6827fffcb955fb4fd5d756daffbea00947c7dcb56725b8862ff4a0dd6
  Stored in directory: c:\users\bobyt\appdata\local\pip\cache\wheels\25\42\45\b773edc52acb16cd2db4cf1a0b47117e2f69bb4eb300ed0e70
Successfully built bs4
Installing collected packages: soupsieve, beautifulsoup4, bs4
Successfully installed beautifulsoup4-4.10.0 bs4-0.0.1 soupsieve-2.3.1





to clear screen use cls






TO check if beautiful soup is installed or not
(myenv) E:\courses\python\webscrapingwithpython\webscraping>python
Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import bs4
>>> exit()






'''