class Solution:
    def generate_results(self, a, b):
        res = [a + b, a - b, b - a, a * b]
        if a:
            res.append(b / a)
        if b:
            res.append(a / b)
        return res
    
    def check(self, cards):
        if len(cards) == 1:
            return abs(cards[0] - 24.0) <= 0.1
        for i in range(len(cards)):
            for j in range(i+1, len(cards)):
                new_list = [number for k, number in enumerate(cards) if (k != i and k != j)]
                for res in self.generate_results(cards[i], cards[j]):
                    new_list.append(res)
                    if self.check(new_list):
                        return True
                    new_list.pop()
        return False
    
    def judgePoint24(self, cards: List[int]) -> bool:
        return self.check(cards)