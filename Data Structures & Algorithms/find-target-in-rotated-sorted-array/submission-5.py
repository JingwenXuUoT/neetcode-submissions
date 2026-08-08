class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left<=right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            if nums[mid]>nums[right]:# pivot at the right half, left half sorted
                if nums[left]<=target<nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
            else: # right half sorted
                if nums[mid]<target<=nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
        # 39~40 ms

        # two parts:
        # 1. which half is sorted, 2. does target fall inside that sorted range?

        # l = 0
        # r = len(nums) - 1

        # while l < r:
        #     m = l + (r - l) // 2
        #     if nums[m] < nums[r]:
        #         r = m
        #     else:
        #         l = m + 1
        # pivot = l

        # def searchHelper(left, right):
        #     if target < nums[left] or target > nums[right]:
        #         return -1
        #     while left < right:
        #         m = left + (right - left) // 2
        #         if target > nums[m]:
        #             left = m + 1
        #         else:
        #             right = m
        #     if nums[left] == target:
        #         return left
        #     return -1

        # left_search = searchHelper(0, pivot - 1)
        # right_search = searchHelper(pivot, len(nums) - 1)

        # return max(left_search, right_search)
        # 46~47 ms
