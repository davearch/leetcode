class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers) -1
        
        while lo < hi:
            curr_sum = numbers[lo] + numbers[hi]
            if curr_sum == target:
                return [lo+1, hi+1]
            elif curr_sum < target:
                lo += 1
            else:
                hi -= 1