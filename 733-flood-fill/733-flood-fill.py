class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_color = image[sr][sc]
        ROW_LENGTH = len(image)
        COL_LENGTH = len(image[0])
        def dfs(r, c) -> None:
            if not image[r][c] == starting_color:
                return
            if image[r][c] == color:
                return
            image[r][c] = color
            if r > 0: dfs(r -1, c) # up
            if c > 0: dfs(r, c -1) # left
            if r < ROW_LENGTH -1: dfs(r +1, c) # down
            if c < COL_LENGTH -1: dfs(r, c +1) # right
        dfs(sr,sc)
        return image