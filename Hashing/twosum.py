'''
https://leetcode.com/problems/two-sum/
'''
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i in range(len(nums)):
            if target-nums[i] not in hashmap:
                hashmap[nums[i]] = i
            else:
                ans = [hashmap[target-nums[i]], i]
        return ans
