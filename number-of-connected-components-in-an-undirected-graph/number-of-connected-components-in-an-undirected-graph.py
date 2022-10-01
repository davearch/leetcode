class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        f = list(range(n))
        r = [1 for _ in range(n)]
        size = n
        
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
                r[b] += 1
        
        for pair in edges:
            node1, node2 = pair
            root1, root2 = find(node1), find(node2)
            if root1 == root2:
                continue
            union(root1, root2)
            size -= 1
        return size