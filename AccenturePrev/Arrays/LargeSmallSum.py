'''
def LargeSmallSum(arr)

The function accepts an integers arr of size ’length’ as its arguments you are required to return the sum of second largest  element from the even positions and second smallest from the odd position of given ‘arr’

Assumption:

All array elements are unique
Treat the 0th position as even

Return 0 if array is empty
Return 0, if array length is 3 or less than 3
Example

Input

arr:3 2 1 7 5 4

Output

7
'''

def LargeSmallSum(arr):
    if len(arr)<=3:
        return 0
    even = []
    odd = []
    for i in range(len(arr)):
        if i==0 or i%2==0:
            even.append(arr[i])
        else:
            odd.append(arr[i])
    even.sort()
    odd.sort()
    return even[len(even)-2] + odd[1]
arr = [1,8,0,2,3,5,6]
print(LargeSmallSum(arr))