class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # two pointers, intialize them at the second position
        # one pointer to tag the last position of the result array, the other is to scan the array
        # stop when right pointer is out of bound
        # O(n), O(1)
        l = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        
        return l