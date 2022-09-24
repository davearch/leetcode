from collections import Counter
from heapq import heappush, nlargest
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = Counter(nums)
                
        minheap = []
        for num, count in numCount.items():
            heappush(minheap, (count, num))
        return [pair[1] for pair in nlargest(k, minheap)]