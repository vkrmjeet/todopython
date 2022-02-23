'''
    it is also known as 2d list
       collection of list each list is an item
       each list is a row with columns within the collection
       the index starts from zero
'''


fruits=[["apple","banana"],
        ["peach","mango"],
        ["orange","pineapple"]
        ]
print(fruits[1][1])   #this will print mango in the output

for row in fruits:
    for col in row:
        print(col)