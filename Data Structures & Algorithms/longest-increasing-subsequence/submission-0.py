class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] means the length of the longest increasing subsequence ending at i
        # tracking a globle maxLen
        # for each step j, check i in range(j), dp[j] = 1 + max(dp[i]) if nums[j]>nums[i], update maxLen
        # return maxLen
        # O(n^2)

        n = len(nums)
        dp = [1] * n
        maxLen = 1

        for j in range(n):
            for i in range(j):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], dp[i]+1)
            maxLen = max(maxLen, dp[j])
        
        return maxLen
        