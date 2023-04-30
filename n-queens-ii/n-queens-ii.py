class Solution:
    def point_not_under_attack(self, row, col):
        if row in self.rows or \
            col in self.cols or \
            row + col in self.l_diags or \
            row - col in self.r_diags:
            return False
        return True
    
    def place_queen(self, row, col):
        self.rows.add(row)
        self.cols.add(col)
        self.l_diags.add(row + col)
        self.r_diags.add(row - col)
    
    def remove_queen(self, row, col):
        self.rows.remove(row)
        self.cols.remove(col)
        self.l_diags.remove(row + col)
        self.r_diags.remove(row - col)
    
    def totalNQueens(self, n: int) -> int:
        self.rows = set()
        self.cols = set()
        self.l_diags = set()
        self.r_diags = set()
        
        def helper(row = 0, count = 0):
            for col in range(n):
                if self.point_not_under_attack(row, col):
                    self.place_queen(row, col)
                    if row == n - 1:
                        count += 1
                    else:
                        count = helper(row + 1, count)
                    self.remove_queen(row, col)
            return count
        return helper()