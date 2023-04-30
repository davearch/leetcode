class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        """
        each row is double in size of the previous
        recurrence relation: rec(n, k) => rec(n - 1, prevk)
        n = 3,
        0 = 2^0
        01 = 2^1
        0110 = 2^2
        01101001 = 2^3
        
        if k is odd: prevk = k // 2 + 1
        if k i even: prevk = k // 2
        
        if k is odd: k => prevk flipped
        if k is even: k => prevk

        n: 2
        k: 1
        output: 0
        
        0
        01
        
        """
        def helper(n: int, k: int) -> int:
            if n == 1:
                return 0
            if k % 2 == 1:
                prevk = helper(n-1, k // 2 + 1)
                return prevk
            else:
                prevk = helper(n-1, k // 2)
                return 1 if prevk == 0 else 0
        return helper(n, k)
                