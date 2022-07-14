class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count, i = {}, 0
        for key, value in enumerate(fruits):
            count[value] = count.get(value, 0) + 1
            if (len(count) > 2):
                count[fruits[i]] -= 1
                if (count[fruits[i]] == 0):
                    del count[fruits[i]]
                i += 1
        return key - i + 1