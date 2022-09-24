from itertools import product
class Solution:
    """
    [[".",".",".",".","5",".",".","1","."],
     [".","4",".","3",".",".",".",".","."],
     [".",".",".",".",".","3",".",".","1"],
     ["8",".",".",".",".",".",".","2","."],
     [".",".","2",".","7",".",".",".","."],
     [".","1","5",".",".",".",".",".","."],
     [".",".",".",".",".","2",".",".","."],
     [".","2",".","9",".",".",".",".","."],
     [".",".","4",".",".",".",".",".","."]]
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidRow(row: int, col: int) -> bool:
            curr_char = board[row][col]
            for i in range(len(board[row])):
                if i == col:
                    continue
                if board[row][i] == curr_char:
                    return False
            return True

        def isValidCol(row: int, col: int) -> bool:
            curr_char = board[row][col]
            for i in range(len(board)):
                if i == row:
                    continue
                if board[i][col] == curr_char:
                    return False
            return True

        def isValidGrid(row: int, col: int) -> bool:
            # get lowest bound row and col
            grid_row = row - (row % 3)
            grid_col = col - (col % 3)
            
            if (grid_row, grid_col) in grid_memo:
                return grid_memo[(grid_row, grid_col)]
            
            seen = set()
            for i, j in product(range(3), range(3)):
                if board[grid_row + i][grid_col + j] == '.':
                    continue
                if board[grid_row + i][grid_col + j] in seen:
                    grid_memo[(grid_row, grid_col)] = False
                    return False
                seen.add(board[grid_row + i][grid_col + j])
            grid_memo[(grid_row, grid_col)] = True
            return True
        
        grid_memo = {}
        ROWS = len(board)
        COLS = len(board[0])
        
        for row, col in product(range(ROWS), range(COLS)):
            if board[row][col] == '.':
                continue

            if not (isValidRow(row, col) \
                and isValidCol(row, col) \
                and isValidGrid(row, col)):
                return False
        return True