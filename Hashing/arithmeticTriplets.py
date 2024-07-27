class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        valHash = [False]*201
        count = 0
        for i in nums:
            valHash[i] = True
        
        for i in nums:
            if (i<=200 and i+diff<=200 and i+(diff*2)<=200 ):
                if (valHash[i] and valHash[i+diff] and valHash[i+(diff*2)]):
                    count+=1
        return count