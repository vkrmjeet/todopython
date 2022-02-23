'''
    it is a good practice to specify how exceptions will be handled by our program
    if we don't specify then python will use its built in exception handling
    and they aren't user friendly

    error can be handled or caught by embedding your code in
    try and except statement blocks
    there should be atleast 1 except block for it to work for multiple try statement also.

    the handlers for the specific errors are paced inside the except block

    the default python handler is called when no handler is specified
'''

'''
    keywords:
        try block : it lets you test a block of code for errors
        
        except block : it is used to specify how to handle errors 
        
        finally block : it is used to specify what code will execute regardless
                        of what happens in try and except.
        
        else block : it lets you specify what code to execute if no exceptions error occurs.
                     this is optional and not necessary for our exception handling to work.
'''

'''
     example :
            try: code to test for errors
            except: code to execute to handle errors
            finally: code to execute regardless of errors
            else: code to execute if no error occurs
'''