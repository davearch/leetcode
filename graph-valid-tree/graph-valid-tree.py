class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        f = [i for i in range(n)]
        r = [1 for _ in range(n)]
        
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
            
            find(a) == find(b)
        
        for node1, node2 in edges:
            root1 = find(node1)
            root2 = find(node2)
            if root1 == root2:
                return False
            union(root1, root2)
        return True if len(set([find(x) for x in f])) == 1 else False
