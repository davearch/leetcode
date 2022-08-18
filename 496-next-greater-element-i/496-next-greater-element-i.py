class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        numToGreaterDict = {}
        
        for num in nums2:
            while stack and num > stack[-1]:
                numToGreaterDict[stack.pop()] = num
            stack.append(num)
        
        while stack:
            numToGreaterDict[stack.pop()] = -1
        
        res = [0] * len(nums1)
        for i in range(len(nums1)):
            res[i] = numToGreaterDict[nums1[i]]
        return res