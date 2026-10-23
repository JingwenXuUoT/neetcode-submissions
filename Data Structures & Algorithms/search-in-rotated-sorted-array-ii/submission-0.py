class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # comparing to I, the hard part is the duplication mke it hard to identify whether mid belongs to the right or left sorted portion, unable to eliminate half of the search range in some ->
        # but when mid == left, and target is not mid, l = l + 1
        # when left < mid, we can elimate half of the array, l = mid + 1(target> mid) in this case
        l,r = 0, len(nums)-1
        while l<= r:
            m = l +(r-l)//2
            if nums[m] == target:
                return True
            if nums[l]< nums[m]:
                # left portion
                if nums[l] <= target<nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[l] > nums[m]:
                # right portion
                if nums[m] < target<=nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                l += 1
        return False
