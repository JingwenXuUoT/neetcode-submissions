class Solution:
    def findMin(self, nums: List[int]) -> int:
        # length = len(nums)
        
        # left = 0
        # right = length-1
        # while(left<right):
        #     mid = left + (right-left) // 2 # use integer division instead of float division '/' to avoid decimal indices
        #     if(nums[mid]>=nums[left]): # this is always true in an sorted but unrotated array, so  comparing with left would miss the mimimum
        #         left = mid+1
        #     else:
        #         right = mid
        
        # return min(nums[left], nums[right])

        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]



