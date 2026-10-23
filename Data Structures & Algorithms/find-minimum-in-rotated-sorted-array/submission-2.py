class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if nums[m] >= nums[l], the minimum is that the right part m+1..r
        res = nums[0]
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l]< nums[r]:
                # the array is still sorted end-to-end
                res = min(res, nums[l])
                break
            m = (l + r) // 2
            res = min(res, nums[m]) # each mid is a valid candidate
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
