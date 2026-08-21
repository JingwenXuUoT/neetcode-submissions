class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # greedy, discard the negative num
        # for each step, either add current num, extend the subarray; or rest curSum to surrent num
        # return maxSum

        n = len(nums)
        maxSum = nums[0]
        curSum = 0
        for i in range(n):
            # decision: whether the prefic sum worth keeping
            # always sum current num
            if curSum < 0:
                curSum = 0
            curSum += nums[i]
            maxSum = max(maxSum, curSum)
        
        return maxSum