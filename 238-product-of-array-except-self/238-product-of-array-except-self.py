class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [1,  2, 3, 4]
         1   1  2  6
         24  12 4  1
         
        24, 12, 8, 6
        """
        L = [1 for _ in range(len(nums))]
        R = [1 for _ in range(len(nums))]
        
        for i in range(len(nums)):
            if i != len(nums) - 1:
                L[i+1] = nums[i] * L[i]
        for i in range(len(nums)-1, -1, -1):
            if i != 0:
                R[i-1] = nums[i] * R[i]
        
        output = []
        for i in range(len(nums)):
            output.append(L[i] * R[i])
        return output