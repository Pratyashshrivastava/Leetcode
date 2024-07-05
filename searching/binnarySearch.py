''' Time Complexity = O(log2(n))'''

# Iterative Approach:
def search(nums, target) :
    low = 0
    high = len(nums)-1

    while (low <= high):
        mid = (low+high)//2

        if(target == nums[mid]):
            return mid
        elif (target<nums[mid]):
            high = mid-1
        else:
            low = mid + 1
    return -1

# Recursive Approach:

class Solution:
    def Rsearch(self, arr: List[int], low: int, high: int, target: int) -> int:
        if low > high:
            return -1

        mid = (low + high) // 2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            return self.Rsearch(arr, mid + 1, high, target)
        return self.Rsearch(arr, low, mid - 1, target)

    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        return self.Rsearch(nums, low, high, target)

# OverFlow case:
''' if the arr is [0, INT_MAX] then 
        mid = low + high //2 
        and if low == INT_MAX then mid = INT_MAX + INT_MAX // 2 
        then mid = 2*INT_MAX //2 which is not possible

        so we use
        mid = low + (high - low)//2
        which ultimately means 
        mid = 2*low + high - low // 2 = low+high//2
    '''