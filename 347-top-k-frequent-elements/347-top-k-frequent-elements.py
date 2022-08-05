class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        minHeap = []
        for num, count in counter.items():
            if len(minHeap) < k:
                heapq.heappush(minHeap, (count, num))
            else:
                if count > counter[minHeap[0][1]]:
                    heapq.heappushpop(minHeap, (count, num))
        output = []
        for pair in minHeap:
            count, num = pair
            output.append(num)
        return output