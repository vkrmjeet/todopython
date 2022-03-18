'''
     django models are python classes that allows us to save data inside a database.
     each object is a row in a table.
     a model is the single source of information about your data.
     a model contains essential fields and behaviours of the data you are storing.
     each model maps to a single database table.
     each model is a python class that subclasses django.db.models.Model.
     each attribute of a model represent a database field.


     ex: from django.db import models

        class person(models.Model):
             firstname = models.CharField(max_length=30)
             lastname = models.CharField(max_length=30)

     The above model defines a person with a first name and a lastname.
     each field defines a attribute and each attributes maps to a column in the database.
     let us see the table in which this model will be storing data

       CREATE TABLE myapp_person (
          "id" serial NOT NULL PRIMARY KEY,
          "firstname" varchar(30) NOT NULL,
          'lastname" varchar(30) NOT NULL,
          );
'''