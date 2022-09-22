class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        if not mat:
            return []
        
        memo = {}
        ans = [[-1 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        I_TOP_BOUND = 0
        I_LOWER_BOUND = len(mat)-1
        J_LEFT_BOUND = 0
        J_RIGHT_BOUND = len(mat[0]) -1
        for i in range(len(mat)):
            i_range = (max(I_TOP_BOUND, i-k), min(I_LOWER_BOUND, i+k))
            for j in range(len(mat[i])):
                curr_char = mat[i][j]
                j_range = (max(J_LEFT_BOUND, j-k), min(J_RIGHT_BOUND, j+k))
                _sum = 0
                curr_range = (i_range, j_range)
                if curr_range in memo:
                    _sum = memo[curr_range]
                    ans[i][j] = _sum
                    continue
                else:
                    for r in range(i_range[0], i_range[1]+1):
                        for c in range(j_range[0], j_range[1]+1):
                            _sum += mat[r][c]
                memo[curr_range] = _sum
                ans[i][j] = _sum
        return ans