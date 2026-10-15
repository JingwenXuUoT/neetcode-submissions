class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # TC:O(n), SC:O(n)->O(1)
        # reverse overall + reverse each part
        k = k % len(nums)

        # step1
        l, r = 0, len(nums)-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1
        # step2
        l, r = 0, k-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1
        l, r = k, len(nums)-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1

        