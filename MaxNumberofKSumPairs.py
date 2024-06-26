from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        count = 0
        r = len(nums)-1

        while(l<r):
            if nums[l]+nums[r] == k:
                count+=1
                nums.pop(r)
                nums.pop(l)
                # l+=1
                r-=2
            else:
                r-=1
        return count

nums = [3,1,3,4,3]
k = 6
solution = Solution()

print(solution.maxOperations(nums,k))