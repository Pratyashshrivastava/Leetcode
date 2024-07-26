'''
A carry is a digit that is transferred to left if sum of digits exceeds 9 while adding two numbers from right-to-left one digit at a time

You are required to implement the following function.

Int NumberOfCarries(int num1 , int num2);

The functions accepts two numbers ‘num1’ and ‘num2’ as its arguments. You are required to calculate and return  the total number of carries generated while adding digits of two numbers ‘num1’ and ‘ num2’.

Assumption: num1, num2>=0

Example:

Input
Num 1: 451
Num 2: 349
Output
2
Explanation:

Adding ‘num 1’ and ‘num 2’ right-to-left results in 2 carries since ( 1+9) is 10. 1 is carried and (5+4=1) is 10, again 1 is carried. Hence 2 is returned.
'''

def numberOfCarries(num1, num2):
    count = 0
    carry = 0
    while num1 >0 or num2 >0:
        digit1 = num1%10
        digit2 = num2%10

        total = digit1 + digit2 + carry
        
        if total>9:
            count+=1
            carry = 1
        else:
            carry = 0
        
        num1//=10
        num2//=10

    return count

num1 = 476
num2 = 576
print(numberOfCarries(num1,num2))