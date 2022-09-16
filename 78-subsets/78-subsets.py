from copy import deepcopy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        self.backtrack(nums, [], results, 0)
        return results
    def backtrack(self, nums, tempList, results, index):
        results.append(deepcopy(tempList))
        for i in range(index, len(nums)):
            tempList.append(nums[i])
            self.backtrack(nums, tempList, results, i+1)
            tempList.pop()