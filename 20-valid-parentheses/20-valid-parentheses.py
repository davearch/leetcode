class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for char in s:
            if char in closeToOpen:
                top_element = stack.pop() if stack else '#'
                if closeToOpen[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack