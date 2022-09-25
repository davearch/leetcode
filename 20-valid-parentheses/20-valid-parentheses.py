class Solution:
    def isValid(self, s: str) -> bool:
        endCounts = {')': 0, '}': 0, ']': 0}
        openToClose = {'(': ')', '{': '}', '[': ']'}
        closes = []
        for i in range(len(s) -1,-1,-1):
            if s[i] in endCounts.keys():
                closes.append(s[i])
            else:
                if not closes:
                    return False
                closer = closes.pop()
                if openToClose[s[i]] != closer:
                    return False
        return True if not closes else False