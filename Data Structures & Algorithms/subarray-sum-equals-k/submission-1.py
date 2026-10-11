class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
    # we need to maintain the prefixsum wile constructing the result
        res = 0
        curSum = 0
        prefixSums = {0:1} # base case: an empty array
        for num in nums:
            curSum += num
            diff = curSum - k

            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
        
        return res
        