'''
char*MoveHyphen(char str[],int n);

The function accepts a string “str” of length ‘n’, that contains alphabets and hyphens (-). Implement the function to move all hyphens(-) in the string to the front of the given string.

NOTE:- Return null if str is null.

Example :-

Input:
str.Move-Hyphens-to-Front
Output:
—MoveHyphenstoFront
Explanation:-

The string “Move-Hyphens -to-front” has 3 hyphens (-), which are moved to the front of the string, this output is “— MoveHyphen”

Sample Input

Str: String-Compare
Sample Output-

-StringCompare
'''

def moveHyphens(s):
    if len(s)==0:
        return 0
    removed = ''
    count = 0
    for i in s:
        if i == '-':
            count+=1
        else:
            removed+=i
    return '-'*count+removed

s = 'String- Compare'
print(moveHyphens(s))