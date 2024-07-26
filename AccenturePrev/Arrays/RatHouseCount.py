'''
Example:

Input:

r: 7
unit: 2
n: 8
arr: 2 8 3 5 7 4 1 2
Output:

4

Explanation:
Total amount of food required for all rats = r * unit

= 7 * 2 = 14.

The amount of food in 1st houses = 2+8+3+5 = 18. Since, amount of food in 1st 4 houses is sufficient for all the rats. Thus, output is 4.
'''


def calculate(arr, r, unit,n):
    totalFootRequired = r*unit
    HouseRequired = 0
    currCount = 0

    if n == 0:
        return -1
    for i in range(n):
        currCount+=arr[i]

        if currCount>= totalFootRequired:
            return i+1
    if currCount< totalFootRequired:
        return 0

def main():
    r = int(input())
    unit = int(input())
    n = int(input())
    arr = list(map(int,input().split()))
    print(calculate(arr,r,unit,n))

main()