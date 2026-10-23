class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if mid is in left sorted part, and target is larger than mid, move l to m+1; if target is smaller than mid, if target is smaller than the minimum in left part nums[l], then move is in the right part; other wise, binary search in the left part->r=mid-1
        # draw a index-num[index] graph is helpful
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r)//2
            if target == nums[mid]:
                return mid
            # left sorted portion
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target< nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target<nums[mid] or target >nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1


