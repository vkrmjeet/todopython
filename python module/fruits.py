'''
    this file is used to access the packages that are in the module
'''

import example.foo

example.foo.fruits("apple")

#this is the first method and we can also use from keyword.

from example import foo
foo.fruits("banana")