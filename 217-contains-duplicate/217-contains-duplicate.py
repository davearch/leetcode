class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        given an array of nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
        
        [1,2,3,1] => true
        [1,2,3,4] => false
        [1,1,1,3,3,4,3,2,4,2] => true
        1 <= nums.length <= 10^5
        -10^9 <= nums[i] <= 10&^9
        
        [] => throws exception
        [1] => false
        [1,1] => true
        [-1,1] => false
        [0, 0, 0] => true
        
        [1,...99999999]
        """
        # O(n) -> time, O(n) -> space
        s = set()
        for num in nums:
            if num not in s:
                s.add(num)
            else:
                return True
        return False