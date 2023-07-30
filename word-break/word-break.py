class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        s = "applepenapple", wordDict = ["apple","pen"]
        i:0
        loop through wordDict, compare with s starting from i
        
        i: 5
        
        i >= len(s): return True
        dp(i) = dp(i + len(word)) for any word that matches our current index
        """
        def dp(i: int, memo = {}) -> bool:
            if i >= len(s):
                return True
            if i in memo:
                return memo[i]
            res = []
            for word in wordDict:
                if s[i:i + len(word)] == word:
                    res.append(dp(i + len(word), memo))
            memo[i] = any(res)
            return memo[i]
        return dp(0)