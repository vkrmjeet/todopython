'''

    it has a three tree architecture
       1. working directory:- at this stage all the files that are in working category
                are not tracked by git because they aren't pushed to the repository.
            git add . will add the file in staging index. but they are not committed to the repository.
            git commit will push the file to repository.

    git workflow process
        1. we are working on a file and we name it by the naming convention and v1(version1) and perform git add command to add it to staging index.
           for the next step we have to perform command git commit to add it to repository.
        if we have to make changes to the same file then it will be renamed as version 2.
        we can revert back to version 1 also if we have some kind of bug in the version 2.

'''