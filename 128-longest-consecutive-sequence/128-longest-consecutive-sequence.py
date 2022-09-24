class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_path = 0
        num_set = set(nums)
        seen = set()
        for i in range(len(nums)):
            el = nums[i]
            path_sum = 1
            while el + 1 in num_set:
                if el + 1 in seen:
                    break
                path_sum += 1
                seen.add(el + 1)
                el = el + 1
            el = nums[i]
            while el - 1 in num_set:
                if el -1 in seen:
                    break
                path_sum += 1
                seen.add(el - 1)
                el = el - 1
            longest_path = max(longest_path, path_sum)
        return longest_path
