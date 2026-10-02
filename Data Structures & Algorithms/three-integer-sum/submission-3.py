class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] # res is a set to store tuples
        nums.sort() # avoid duplicate nums[i]
        for idx, num in enumerate(nums):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue # avoid duplicate nums[i]

            left = idx+1
            right = len(nums)-1
            while left < right:
                cursum = nums[left] + nums[right] + num
                if cursum == 0:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left<right:
                        left += 1
                elif cursum < 0:
                    left += 1
                else:
                    right -= 1

        return [list(x) for x in res]
    
    # a set can store tuples, but cannot store lists
    # because sets only accept hashable(immutable) items
    # tuples are immutable and can be hashed, while lists are mutalble and unhashable