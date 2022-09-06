from copy import deepcopy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        self.backtrack(result, [], nums, 0)
        return result
    
    def backtrack(self, result, templist, nums, start):
        result.append(deepcopy(templist))
        for i in range(start, len(nums)):
            templist.append(nums[i])
            self.backtrack(result, templist, nums, i+1)
            templist.pop()