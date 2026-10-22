class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # the minimum capacity can choose is the maximum value of weights, and the max capacity is the sum of all of the weights.
        # range of the binary search: (max(weights)..sum(weights))
        l, r = max(weights), sum(weights)
        res = r

        def canShip(cap):
            day, curCap = 1, cap
            for w in weights:
                if curCap - w < 0:
                    day += 1
                    curCap = cap
                curCap -= w
            return day <= days

        while l <= r:
            m = l + (r - l)//2
            if canShip(m):
                res = min(res, m)
                r = m -1
            else:
                l = m + 1
        
        return res
        