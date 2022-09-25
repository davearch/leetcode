class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        [7,1,5,3,6,4]
           ^
                   ^
        curr: 3
        max: 5
        """
        max_profit = 0
        start = 0
        curr_profit = 0
        for end in range(1, len(prices)):
            curr_profit = prices[end] - prices[start]
            if curr_profit < 0:
                start = end
                continue
            max_profit = max(max_profit, curr_profit)
        return max_profit