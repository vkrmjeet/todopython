'''
    django architecture : it used mvc type of architecture. m:model v:view c:control
        it refers to them as url patters,views , templates,models

             url patters:it takes the path as a request and determines which views should handle the request
             views: it is the logic layer of django app, they take the request and returns a http response.
                   each view can use a model which we have defined in our application to query the data.
            template : once we have queried the data it uses templates to show the data.
'''