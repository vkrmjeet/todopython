'''

    system level configuration :- this will apply to every user using the computer.
        git config --system
    user level configuration :- it applies to specific users using the machine.
        git config --global
    project level configuration :- it applies to the whole project.
        git config

in git bash (to set)
     bobyt@MSI MINGW64 ~
$ git config --global user.name "vkrmjeet"

bobyt@MSI MINGW64 ~
$ git config --global user.email "bobythakran@gmail.com"

in git bash (to check)
bobyt@MSI MINGW64 ~
$ git config user.name
vkrmjeet

bobyt@MSI MINGW64 ~
$ git config user.email
bobythakran@gmail.com


in git bash -- to open a directory.

bobyt@MSI MINGW64 ~
$ cd desktop

in git bash -- to list directory

bobyt@MSI MINGW64 ~/desktop
$ ls
 CodeBlocks.lnk*                            Spotify.lnk*
 Kindle.lnk*                                Telegram.lnk*
 MEGAsync.lnk*                              Udeler.lnk*
'New Volume (D) - Shortcut.lnk'*            WhatsApp.lnk*
 P60208-101103.jpg                         'courses - Shortcut.lnk'*
'PyCharm Community Edition 2021.2.3.lnk'*   desktop.ini

in git basg -- to make a new directory

bobyt@MSI MINGW64 ~/desktop
$ mkdir python

in git bash -- to open newly created directory

bobyt@MSI MINGW64 ~/desktop
$ cd python

in git bash -- to create new files

bobyt@MSI MINGW64 ~/desktop/python
$ touch index.html

bobyt@MSI MINGW64 ~/desktop/python
$ touch index.js

in git bash -- to make a new repository

bobyt@MSI MINGW64 ~/desktop/python
$   git init
Initialized empty Git repository in C:/Users/bobyt/Desktop/python/.git/


bobyt@MSI MINGW64 ~/desktop/python (master)
$ cd D:courses/python
bash: cd: D:courses/python: No such file or directory

bobyt@MSI MINGW64 ~/desktop/python (master)
$ cd E:/courses/python

bobyt@MSI MINGW64 /e/courses/python (master)
$ git init
Reinitialized existing Git repository in E:/courses/python/.git/

$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   data structures/dictionary methods.py

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   data structures/dictionary methods.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .idea/
        CONTROL flow/
        basic/
        data structures/accessing elements in a list.py
        data structures/list methods part 2.py
        data structures/listmethods part1.py
        data structures/lists.py
        data structures/nested list (2d list).py
        data structures/python dictionary.py
        data structures/random.py
        data structures/set methods.py
        data structures/set.py
        data structures/tuple.py
        datatype/
        dateandtime/
        ex.py
        ex2.py
        exceptions/
        file handling/
        functions/
        git/
        intro.txt
        oops/
        practice problems/
        python module/
        string methods and formatting/

git add . to add all the files in the staging index.

bobyt@MSI MINGW64 /e/courses/python (master)
$ git rm --cached /oops/intro   to remove fies from the staging index


'''