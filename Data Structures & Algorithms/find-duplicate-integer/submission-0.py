class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = max(nums)
        n_set = set()
        for num in nums:
            if num in n_set:
                return num
            n_set.add(num)
        return n
        