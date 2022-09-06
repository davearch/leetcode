class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        self.backtrack(result, [], nums, 0)
        return result
    
    def backtrack(self, result, templist, nums, start):
        result.append(deepcopy(templist))
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]: continue
            templist.append(nums[i])
            self.backtrack(result, templist, nums, i+1)
            templist.pop()