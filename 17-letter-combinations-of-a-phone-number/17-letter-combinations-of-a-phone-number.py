from collections import deque
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            '2': 'abc', '3': 'def',
            '4': 'ghi', '5':'jkl', '6':'mno',
            '7':'pqrs', '8':'tuv', '9': 'wxyz'
        }
        if not digits:
            return []
        q = deque([])
        q.append([])
        result = []
        for i in range(len(digits)):
            n = len(q)
            for j in range(n):
                curr_digit = digits[i]
                possible_letters = letters[curr_digit]
                old_combo = q.popleft()
                for letter in possible_letters:
                    new_combo = list(old_combo)
                    new_combo.append(letter)
                    if len(new_combo) == len(digits):
                        result.append(''.join(new_combo))
                    else:
                        q.append(''.join(new_combo))
        return result