from collections import Counter
from string import ascii_lowercase
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        count1 = Counter(ascii_lowercase)
        count2 = Counter(ascii_lowercase)
        
        count1.update(word1)
        count2.update(word2)
        
        for key in count1.keys():
            if abs(count1[key] - count2[key]) >= 4:
                return False
        return True