from collections import Counter
from heapq import heappush, heappushpop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = Counter(nums)
        minheap = []
        for num, count in numCount.items():
            if len(minheap) < k:
                heappush(minheap, (count, num))
            else:
                heappushpop(minheap, (count, num))
        return [pair[1] for pair in minheap]