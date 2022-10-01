class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key=lambda x: x[0])
        
        f = list(range(n))
        r = [1 for _ in range(n)]
        
        size = n
        min_time = float('inf')
        
        def find(x):
            if f[x] == x:
                return x
            f[x] = find(f[x])
            return f[x]
        
        def union(a, b):
            if r[a] > r[b]:
                f[b] = a
            elif r[a] < r[b]:
                f[a] = b
            else:
                f[b] = a
                r[a] += 1
        
        for t, n1, n2 in logs:
            r1, r2 = find(n1), find(n2)
            if r1 == r2:
                continue
            union(r1, r2)
            size -= 1
            if size == 1:
                min_time = min(min_time, t)
        return min_time if size == 1 else -1
