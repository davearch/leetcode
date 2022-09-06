from copy import deepcopy
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        used = [False for _ in range(len(nums))]
        self.backtrack(result, [], nums, used)
        return result
    
    def backtrack(self, result, templist, nums, used):
        if len(templist) == len(nums):
            result.append(deepcopy(templist))
        else:
            for i in range(len(nums)):
                if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                    continue
                used[i] = True
                templist.append(nums[i])
                self.backtrack(result, templist, nums, used)
                used[i] = False
                templist.pop()