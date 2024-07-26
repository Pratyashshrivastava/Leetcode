'''
int CheckPassword(char str[], int n);
The function accepts string str of size n as an argument. Implement the function which returns 1 if given string str is valid password else 0.
str is a valid password if it satisfies the below conditions.

– At least 4 characters
– At least one numeric digit
– At Least one Capital Letter
– Must not have space or slash (/)
– Starting character must not be a number
Assumption:
Input string will not be empty.

Example:

Input 1:
aA1_67
Input 2:
a987 abC012

Output 1:
1
Output 2:
0
'''

def checker(str):
    cap = 0
    nu = 0
    if len(str) < 4:
        return 0
    if str[0].isdigit():
        return 0
    for i in range(len(str)):
        if str[i] == ' ' or str[i] == '/':
            return 0
        if str[i]>='A' and str[i]<='Z':
            cap+=1
        elif str[i].isdigit():
            nu+=1
    if cap>0 and nu>0:
        return 1
    else:
        return 0
    
s = input()
print(checker(s))
    
        