'''
    templates in django can consist of static parts of desired HTML output.
    a template also has some special syntax for dynamic content.
        special tag {%tag%} this tag can be used to inject dynamic content.
        special templates variables : {{variable}}
        special template variable and filters : {{variable | filter }}

    adding mockup design template into django.
    this has to be done inside the app directory and a sub directory is to be created
    whose name is templates and then another directory with the same name as app name
    is to be created and index.html file is to be added inside our app directory.

    in our case we have to add todolist in templates app.

    static directory is also created and files like bootstrap and css files
    are added inside the static directory.
    inside template folder static folder should be created and inside that
    a new directory whose name is same as the app name , inside that static files should be kept.
    django will look inside these directories for the files required.

    view function is used to display templates and url patters is also used.
'''