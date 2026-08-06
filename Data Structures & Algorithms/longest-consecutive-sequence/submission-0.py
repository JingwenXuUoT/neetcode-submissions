class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = set(nums)

        for idx, num in enumerate(nums):
            length = 0
            if num-1 not in nums_set:
                curr = num
                while(curr in nums_set):
                    length += 1
                    curr += 1
                longest = max(longest, length)
        
        return longest
