class Solution:
    def rob(self, nums: List[int]) -> int:
        # memo = [-1] * len(nums)
        
        # def dfs(i):
        #     if i>= len(nums):
        #         return 0
            
        #     if memo[i] != -1:
        #         return memo[i]
            
        #     memo[i] = max(dfs(i+1), nums[i]+dfs(i+2))

        #     return memo[i]

        # return dfs(0)

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])
        rob1 = nums[0]
        rob2 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            temp = max(rob2, nums[i] + rob1)
            rob1 = rob2
            rob2 = temp

        return rob2