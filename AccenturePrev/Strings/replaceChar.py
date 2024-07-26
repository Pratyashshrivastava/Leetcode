'''
Void *ReplaceCharacter(Char str[], int n, char ch1, char ch2);

The function accepts a string  ‘ str’ of length n and two characters ‘ch1’ and ‘ch2’ as its arguments . Implement the function to modify and return the string ‘ str’ in such a way that all occurrences of ‘ch1’ in original string are replaced by ‘ch2’ and all occurrences of ‘ch2’  in original string are replaced by ‘ch1’.

Assumption: String Contains only lower-case alphabetical letters.

Note:

Return null if string is null.
If both characters are not present in string or both of them are same , then return the string unchanged.
Example:

Input:
Str: apples
ch1:a
ch2:p
Output:
paales
Explanation:

‘A’ in original string is replaced with ‘p’ and ‘p’ in original string is replaced with ‘a’, thus output is paales.
'''

def replaceChar(str,ch1,ch2):
    new = ''
    for i in str:
        if i == ch1:
            new+=ch2
        elif i == ch2:
            new+=ch1
        else:
            new+=i
    return new

s = 'apple'
ch1 = 'a'
ch2 = 'p'
print(replaceChar(s,ch1,ch2))