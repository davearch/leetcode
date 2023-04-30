class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.n, self.k = n, k
        self.output = []
        self.backtrack()
        return self.output
    
    def backtrack(self, first = 1, curr = []) -> None:
        if len(curr) == self.k:
            self.output.append(curr[:])
        else:
            for i in range(first, self.n + 1):
                curr.append(i)
                self.backtrack(i + 1, curr)
                curr.pop()
                