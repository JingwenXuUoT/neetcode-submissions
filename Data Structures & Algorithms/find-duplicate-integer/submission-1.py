class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # n = max(nums)
        # n_set = set()
        # for num in nums:
        #     if num in n_set:
        #         return num
        #     n_set.add(num)
        # return n
        # O(n), O(n)

        # METHOD 2: Binary Search
        # use binary search on the value range
        # if all numbers from 1 to mid appeared at most once,
        # then the count of numbers <= mid should be <= mid, 
        # otherwise, meaning the duplicate must be in the range [1,mid]
        # continuous shrink the candidate range, when low== high, the value is the result
        # TC: O(nlogn), SC: O(1)
        n = len(nums)
        low = 1
        high = n - 1
        while low < high:
            mid = low + (high - low) // 2
            lessOrEqual = sum( 1 for num in nums if num <= mid)
            if lessOrEqual <= mid:
                low = mid + 1
            else:
                high = mid

        return low
        # method 3: optimize SC to O(1)
        # treating the array as linkedlist
        # from an index i, the next index is nums[i]
        # every value is in the range 1 to len(nums)-1, so every value is also a valid index
        # since one value is repeated, multiple indices point to the same next index.
        # Following the indices starting from index 0 nust therefore lead to a cycle, whose entry corresponds to the duplicate value
        # We can use Floyd's cycle detection algorithm.
        