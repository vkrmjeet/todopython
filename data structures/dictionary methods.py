'''
    dictionary methods:-
        get() :- return the value of specified key
        update() :- insert a specified key:value pair inside the dictionary
        clear()  :- removes all key value pairs from the dictionary
        keys()   :- returns a list of dictionary keys
        values() :- returns a list of dictionary values
        del() :-    deletes the dictionary
'''


#count key value pairs
mycar={"brand":"range rover sports"
        , "model":"hse"
        ,  "year":2017 }
print(mycar)
print(len(mycar))   #this will print the number of key value pairs that are inside the dictionary

#change value of a key
mycar["year"]= 2019   # this will change the value of the key year
print(mycar)

#return value of a specfied key
print(mycar.get("model"))


#update value of a key
mycar.update({"color":"silver"})
print(mycar)


#keys will return all the keys in the dictionary
b=mycar.keys()
print(b)


#values will return all the values in the dictionary
c=mycar.values()
print(c)


#pop will delete the key value pair whose key is specified in it
mycar.pop("color") #this will remove color if nothing was specified then the last key would have been deleted from the dictionary
print(mycar)


#clear will remove all the key value pairs from the dictionary
mycar.clear()
print(mycar)  #this will return an empty dictionary



#del will delete the dictionary as a whole
del mycar
print(mycar)    #this will return that name mycar is not defined as we deleted the said dictionary in the last line