class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        [-2,1,-3,4,-1,2,1,-5,4] => 6
        [1] => 1
        [5,4,-1,7,8] => 23
        [] => throw error
        [1] => 1
        [1,1] = > 2
        [-10_000, 2] => 2
        [999, 999, -10_000] => 2000
        
        """
        # initialize our variables with the first element
        current_subarray = max_subarray = nums[0]
        # start with 2nd element since we already used the first one
        for num in nums[1:]:
            # if current_subarray is negative, throw it away
            # otherwise, keep adding to it
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)
        return max_subarray