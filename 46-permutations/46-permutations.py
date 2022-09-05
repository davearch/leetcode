from collections import deque
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        q = deque([])
        q.append([])
        for num in nums:
            n = len(q)
            for _ in range(n):
                old_perm = q.popleft()
                for j in range(len(old_perm)+1):
                    new = list(old_perm)
                    new.insert(j, num)
                    if len(new) == len(nums):
                        result.append(new)
                    else:
                        q.append(new)
        return result