class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diffs:
                return [diffs[diff], i]
            diffs[nums[i]] = i