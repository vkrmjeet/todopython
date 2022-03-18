'''
    .gitignore file is a file used by git to determine which files or directories to ignore
    it should be committed in the repository for rules to be shared throughout the repository.

    to create a git ignore file
      ex:- touch .gitignore
      it will create a git ignore file
    now let us try to use the gitignore file for that let us create a file
    tobeignored.txt

    for this file to be ignored we have to edit gitignore file
    add line
    tobeignored.txt
    and then tobeignored will not show to be committed in the staging area

    git add .
    this command will not add tobeignored in the staging index 

'''