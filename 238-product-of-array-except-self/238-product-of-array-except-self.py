class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = [1 for _ in range(len(nums))]
        R = [1 for _ in range(len(nums))]
        
        for i in range(len(nums)):
            if i != len(nums) - 1:
                L[i+1] = nums[i] * L[i]
        for i in range(len(nums)-1, -1, -1):
            if i != 0:
                R[i-1] = nums[i] * R[i]
        return [L[i] * R[i] for i in range(len(nums))]