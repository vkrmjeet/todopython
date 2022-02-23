'''binary is a language that computer understands
binary is a system of counting
binary is also known as base 2
'''

#converting numbers to binary
'''if 13 is divided by half consecutively we get 13 6 3 1 and to convert it into binary we take 0 for even numbers 
and 1 for odd numbers so for 13 we get 1101 '''

#converting binary to numbers
'''to convert numbers to binary we need to take the number and convert the binary number by taking its values 
in base 2 format    

so for a binary number 10010   we take pow(2,4) for first digit pow(2,3) for second digit and so on for last digit we
take pow(2,0) and we add the numbers only whose value is 1

so for the above binary number we get 16+2 = 19'''


#converting binary decimal to number decimal
'''
the steps for left side of decimal is same but for the right side of decimal we take 
pow(2,-1) , pow(2,-2),pow(2,-3) and so on..... the power is raised to negative rather than positive
so for a number 1100.101

we get 12 for the left side of decimal 
and for left side of decimal we get 1/2 + 1/8 (we do not add 1/4 because its binary value is 0
we get 0.5 + 0.125 

the total sum we get is 12.625'''