class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 # we are only dealing with positive values, the lower bound is 1
        right = max(piles)
        # so the binary search space is 1 through max(piles)
        res = right

        while left <= right:
            cur_h = 0
            mid = left + (right - left) // 2
            for pile in piles:
                # cur_h += (pile + mid - 1) // mid
                cur_h += math.ceil(pile / mid)
            if cur_h <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res