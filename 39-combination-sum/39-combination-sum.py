class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.backtrack(result, candidates, [], target, 0)
        return result

    def backtrack(self, result, candidates, templist, remain, start):
        if remain < 0: return
        elif remain == 0: result.append(templist[:])
        else:
            for i in range(start, len(candidates)):
                templist.append(candidates[i])
                self.backtrack(result, candidates, templist, remain - candidates[i], i)
                templist.pop()