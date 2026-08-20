class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] means the length of the longest increasing subsequence ending at i
        # tracking a globle maxLen
        # for each step j, check i in range(j), dp[j] = 1 + max(dp[i]) if nums[j]>nums[i], update maxLen
        # return maxLen
        # O(n^2)

        # n = len(nums)
        # dp = [1] * n
        # maxLen = 1

        # for j in range(n):
        #     for i in range(j):
        #         if nums[j] > nums[i]:
        #             dp[j] = max(dp[j], dp[i]+1)
        #     maxLen = max(maxLen, dp[j])
        
        # return maxLen

        # method 2: O(nlogn), using bineary search
        # maintain a seperate array tail, tail[k] holds the smallest possible tail value of any increasing subsequence of length k+1 seen so far.
        # for each new number, binary search for where it fits in tails and eother extend tails or replace en entry
        # the length of tails at the end is the answer
        import bisect
        tails = [] # always sorted
        for x in nums:
            i = bisect.bisect_left(tails, x)
            # locates the index for a target value in a sorted list, return the index before any exisiting entries, use binary search
            if i == len(tails):
                tails.append(x)
            else:
                tails[i] = x
        return len(tails)
        