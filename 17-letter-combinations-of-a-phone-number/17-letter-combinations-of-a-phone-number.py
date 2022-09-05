class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            '2': 'abc', '3': 'def',
            '4': 'ghi', '5':'jkl', '6':'mno',
            '7':'pqrs', '8':'tuv', '9': 'wxyz'
        }
        if not digits:
            return []
        n = len(digits)
        result = []
        def helper(index, path):
            if len(path) == len(digits):
                result.append(''.join(path))
                return
            possible_letters = letters[digits[index]]
            for letter in possible_letters:
                path.append(letter)
                helper(index+1, path)
                path.pop()
        helper(0, [])
        return result