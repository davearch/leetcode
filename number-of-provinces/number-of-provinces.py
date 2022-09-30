from itertools import product
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
      0 [1,1,0]
      1 [1,1,0]
      2 [0,0,1]
         0 1 2
         
        [0 0 2]
         0 1 2
        """
        n = len(isConnected)
        f = [i for i in range(n)]
        r = [1 for _ in range(n)]
        def find(x):
            if f[x] == x:
                return x
            f[x] = find(f[x])
            return f[x]
        
        for row, col in product(range(n), range(n)):
            if row == col:
                continue
            row_root, col_root = find(row), find(col)
            if row_root == col_root:
                continue
            if isConnected[row][col]:
                if r[col_root] > r[row_root]:
                    f[col_root] = row_root
                elif r[col_root] < r[row_root]:
                    f[row_root] = col_root
                else:
                    f[col_root] = row_root
                    r[col_root] += 1
        return len(set(f))
                