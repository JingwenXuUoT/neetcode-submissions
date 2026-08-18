class Solution:
    def rob(self, nums: List[int]) -> int:
        # bottom-up DP
        # split the problem into two linear cases:
        # rob houses from index 1 to n-1
        # rob houses from index 0 to n-2
    
        def helper(nums):
            # House Robber I
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]
            
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], nums[i]+dp[i-2])
            
            return dp[-1]

        # only one house, return value
        if len(nums) == 1:
            return nums[0]
        
        # two cases
        # each case: dp[i] means maximum money up to house 1
        # transition: dp[i] = max(dp[n-1], nums[i]+dp[n-2])
        # return max of both cases

        return max(helper(nums[1:]), helper(nums[:-1]))