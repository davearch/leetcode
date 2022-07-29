class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rcount = Counter(map(tuple, grid))
        ccount = Counter(zip(*grid))
        
        ans = 0
        for k, v1 in rcount.items():
            v2 = ccount[k]
            ans += v1 * v2
        return ans