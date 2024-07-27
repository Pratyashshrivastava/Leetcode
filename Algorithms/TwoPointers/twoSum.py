'''
https://leetcode.com/problems/two-sum/

provided that the array should be sorted
'''

def twoSum(nums, target) :
    nums.sort()
    l = 0
    h = len(nums)-1
    while (l<=h):
        if nums[l]+nums[h] > target:
            h-=1
        elif nums[l]+nums[h]<target:
            l+=1
        else:
            return [l,h]
        

