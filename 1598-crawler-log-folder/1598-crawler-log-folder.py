class Solution:
    def minOperations(self, logs: List[str]) -> int:
        if not logs:
            return 0

        stack = []
        for move in logs:
            if move == './':
                continue
            if move == '../':
                if stack:
                    stack.pop()
                continue
            stack.append(move)
        return len(stack)