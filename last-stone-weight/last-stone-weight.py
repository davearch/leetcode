class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones: return 0
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            stoneY = heapq.heappop(stones) * -1
            stoneX = heapq.heappop(stones) * -1
            if stoneX == stoneY:
                continue
            elif stoneX != stoneY:
                stoneY = (stoneY - stoneX) * -1
                heapq.heappush(stones, stoneY)
        return stones[0] *-1 if stones else 0