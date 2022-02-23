'''bitwise AND &
set each bit with matching value if value doesnt match it sets it to 0
x   |    y     |   x&y
0   |    0     |   0
0   |    1     |   0
1   |    0     |   0
1   |    1     |   1

'''

5&4  #this will work on python console and returns the value 4

'''5= 101  && 4=100  if we apply bitwise & then only 100 matches thats why it returns 100 or 4 as its output'''


'''bitwise OR |
 set each bit with matching value if value doesnt match it sets it to 1 if one of them is 1
x   |    y     |   x&y
0   |    0     |   0
0   |    1     |   1
1   |    0     |   1
1   |    1     |   1
'''

5 | 4 # this will work in python console and returns value 5
'''5= 101  && 4=100  if we apply bitwise | then 101 matches and it returns 101 or 5 as its output'''


'''bitwise XOR ^
it returns 1 if numbers do not match and returns 0 if they match
x   |    y     |   x&y
0   |    0     |   0
0   |    1     |   1
1   |    0     |   0
1   |    1     |   1
'''

5 ^ 4 # this will return 1 in python console
''' ad 5 =101 and 4= 100   they are only different in the unit position thats why it returns 1 '''



'''bitwise NOT ~ 
it inverts bits
if i have value x it returns x-(x+1) 
for 7 it gives negative 8
'''
~7 # this will return 8 in python console



'''LEFT SHIFT OPERATOR <<
returns x with the bits shifted to the left by y places
'''
3<<2  #it will shift the binary value of 3 which is 11 to 2 places to the right and add 2 zeroes
      # the new number becomes 1100 whose decimal value is 12




'''right shift operator >> 
it removes bits from the value , it returns the bits shifted to the right by y places
'''

3>>1 #this will return value 1 as the binary value of 3 is 11 it is shifted to the right by 1 place and 0 is added in
     # in front of it so we are left with 01 binary value whose decimal value is also 1