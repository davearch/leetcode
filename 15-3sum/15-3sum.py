class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        nums.sort()
        print(nums)
        for i in range(len(nums)):
            j = i+1
            k = len(nums) -1
            while j < k:
                _sum = nums[i] + nums[j] + nums[k]
                if _sum == 0:
                    output.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif _sum < 0:
                    j += 1
                else:
                    k -= 1
        return [list(tup) for tup in output]