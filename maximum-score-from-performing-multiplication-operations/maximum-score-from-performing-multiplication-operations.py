class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        """
        dp(i, j) = maximum score from all previous i, j pairs
        dp(steps, left) = max(
            dp[steps + 1, left + 1] + multipliers[steps] * nums[left],
            dp[steps + 1, left] + multipliers[steps] * nums[right]
            )
        """
        n, m = len(nums), len(multipliers)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        
        for step in range(m - 1, -1, -1):
            for left in range(step, -1, -1):
                mult = multipliers[step]
                right = n - 1 - (step - left)
                dp[step][left] = max(
                    mult * nums[left] + dp[step + 1][left + 1],
                    mult * nums[right] + dp[step + 1][left]
                )
        return dp[0][0]