class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        self.backtrack(n, [], result, k, 1)
        return result
    
    def backtrack(self, remaining, templist, result,  k, startIndex):
        if remaining == 0:
            if len(templist) == k:
                result.append(templist[:])
        elif remaining < 0:
            return
        else:
            for i in range(startIndex, 10):
                templist.append(i)
                self.backtrack(remaining - i, templist, result, k, i+1)
                templist.pop()