from typing import List
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        l=0
        # r = 1
        ans = []
        ch = 0
        while ch<len(words[l]):
            count = 1
            for r in range(1,len(words)):
                if (words[l][ch] in words[r]):
            # while (words[l][ch] in words[r] and r<len(words)):
                    count+=1
                    # r+=1
                if(count == len(words)): 
                    ans.append(words[l][ch])
            else:
                ch+=1
                # r = 1
        # if (l<len(words)):
        #     l+=1 
        # else: 
        return ans
            
words = ["bella","label","roller"]
solution = Solution()
returnVal = solution.commonChars(words)
print(returnVal)