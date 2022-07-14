class Solution:
    def swap(self, nums: List[int], i: int, j:int) -> None:
        nums[i], nums[j] = nums[j], nums[i]
    
    def reverse(self, nums: List[int], start:int) -> None:
        i, j = start, len(nums) -1
        while (i < j):
            self.swap(nums, i, j)
            i += 1
            j -= 1
    
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while (i >= 0 and nums[i+1] <= nums[i]):
            i -= 1
        if (i >= 0):
            j = len(nums) - 1
            while (nums[j] <= nums[i]):
                j -= 1
            self.swap(nums, i, j)
        self.reverse(nums, i+1)
        