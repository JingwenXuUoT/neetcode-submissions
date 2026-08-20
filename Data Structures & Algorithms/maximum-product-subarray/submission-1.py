class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        # product[i][j] means the subarray product from index i to index j
        cur_max = nums[0]
        cur_min = nums[0]
        # also the whole product table is not used, obly one row would be used, and specifically two numbers per step, not even the whole array
        # -> walk left to right, "what's the best and worst product of a subarry ending exactly at j"
        # product should be initialized as a 2D square with diagnal seed
        maxProduct = nums[0] # when all products are negative, real product woulf be overridden by 0
        # only track max is not enough in product, because a large negative multiple another negative cloud turn into a large posistive, so minnimum also need to be tracked
        for num in nums[1:]:
            #for each step, three ways a subarray ending here could be built:
            # 1. start frech with just num
            # 2. extend the previous most-positive run
            # 3. extend the previous most-negative run
            candidates = (num, cur_max * num, cur_min * num)
            cur_max = max(candidates)
            cur_min = min(candidates)
            maxProduct = max(maxProduct, cur_max)
        
        return maxProduct
