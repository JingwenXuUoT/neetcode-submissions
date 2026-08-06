class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix_prod = [1] * length
        suffix_prod = [1] * length

        for i in range(1, length):
            prefix_prod[i] = prefix_prod[i-1] * nums[i-1]
        
        for i in range(length-2, -1, -1):
            suffix_prod[i] = suffix_prod[i+1] * nums[i+1]

        res = [1] * length
        for i in range(length):
            res[i] = prefix_prod[i] * suffix_prod[i]
        
        return res
        # or
        # return [prefix[i] * suffix[i] for i in range(n)]
        