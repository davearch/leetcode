class Solution:
    def hammingWeight(self, n: int) -> int:
        _sum = 0
        while (n != 0):
            _sum += 1
            n &= n-1
        return _sum