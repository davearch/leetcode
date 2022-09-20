class Solution:
    def reverseWords(self, s: str) -> str:
        wordList = s.split(" ")
        wordList.reverse()
        comprehension = [word for word in wordList if word != '']
        newString = ' '.join(comprehension)
        return newString
