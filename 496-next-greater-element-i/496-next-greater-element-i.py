class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = {}
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                nextGreater[stack.pop()] = num
            stack.append(num)
        while stack:
            nextGreater[stack.pop()] = -1
        
        output = []
        for num in nums1:
            output.append(nextGreater[num])
        return output