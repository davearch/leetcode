class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.backtrack(candidates, result, [], target, 0)
        return result
    
    def backtrack(self, candidates, result, templist, remaining, startIndex):
        if remaining == 0: result.append(templist[:])
        elif remaining < 0: return
        else:
            for i in range(startIndex, len(candidates)):
                if i > startIndex and candidates[i] == candidates[i-1]:
                    continue
                templist.append(candidates[i])
                self.backtrack(candidates, result, templist, remaining - candidates[i], i+1)
                templist.pop()