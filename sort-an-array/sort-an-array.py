class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        pivot = len(nums) // 2
        left = self.sortArray(nums[:pivot])
        right = self.sortArray(nums[pivot:])
        return self.merge(left, right)
    
    def merge(self, l1: list[int], l2: list[int]) -> list[int]:
        p1, p2 = 0, 0
        output = []
        while p1 < len(l1) and p2 < len(l2):
            if l1[p1] < l2[p2]:
                output.append(l1[p1])
                p1 += 1
            else:
                output.append(l2[p2])
                p2 += 1
        if p1 < len(l1): output.extend(l1[p1:])
        if p2 < len(l2): output.extend(l2[p2:])
        return output
            
            