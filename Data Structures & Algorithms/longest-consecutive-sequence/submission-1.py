class Solution:
    # method1: sort, O(nlogn)
    # trick: visualize the sequence on a number axis
    # the start of the sequence has no left neighbor->requires a O(1) lookup throughout nums
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = set(nums)

        for num in nums:
            length = 0
            if num-1 not in nums_set:
                # if the num is not a candidate of the start of a new sequence, skip it and trying to find the start of the sequence this num belongs
                curr = num # the start of a new sequence
                while(curr in nums_set):
                    length += 1
                    curr += 1 # indicate the expected next consecutive number
                longest = max(longest, length)
        
        return longest
