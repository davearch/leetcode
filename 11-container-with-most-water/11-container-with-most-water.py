class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        lo, hi = 0, len(height) -1
        while lo < hi:
            minHeight = min(height[lo], height[hi])
            area = minHeight * (hi - lo)
            max_water = max(max_water, area)
            if height[hi] < height[lo]:
                hi -= 1
            else:
                lo += 1
        return max_water