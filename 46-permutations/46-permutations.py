from copy import deepcopy
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack(result, [], nums)
        return result
    
    def backtrack(self, result, templist, nums):
        if len(templist) == len(nums):
            result.append(deepcopy(templist))
            return
        for i in range(len(nums)):
            if nums[i] in templist: continue
            templist.append(nums[i])
            self.backtrack(result, templist, nums)
            templist.pop()
            
            