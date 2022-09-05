from collections import deque
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        q = deque([])
        q.append([])
        result = []
        for num in nums:
            n = len(q)
            for _ in range(n):
                old_permutation = q.popleft()
                for i in range(len(old_permutation)+1):
                    new_permutation = list(old_permutation)
                    new_permutation.insert(i, num)
                    if len(new_permutation) == len(nums):
                        result.append(new_permutation)
                    else:
                        q.append(new_permutation)
        return result