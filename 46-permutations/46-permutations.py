class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def backtrack(first = 0):
            if first == n:
                result.append(nums[:])
                return
            for i in range(first, n):
                nums[i], nums[first] = nums[first], nums[i]
                backtrack(first+1)
                nums[i], nums[first] = nums[first], nums[i]
        result = []
        backtrack()
        return result