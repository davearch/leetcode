class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        prefix_sum = [[0] * (n+1) for _ in range(m+1)]
        
        # build 2D prefix_sum
        for i in range(1, m+1):
            for j in range(1, n+1):
                prefix_sum[i][j] = mat[i-1][j-1] + \
                    prefix_sum[i-1][j] + \
                    prefix_sum[i][j-1] - \
                    prefix_sum[i-1][j-1]
        
        ans = [[0] * n for _ in range(m)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                end_i = min(m, i+k)
                end_j = min(n, j+k)
                
                start_i = max(1, i-k)
                start_j = max(1, j-k)
                
                ans[i-1][j-1] = prefix_sum[end_i][end_j] - \
                    prefix_sum[start_i-1][end_j] - \
                    prefix_sum[end_i][start_j-1] + \
                    prefix_sum[start_i-1][start_j-1]

        return ans