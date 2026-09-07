class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # for each candidate starting point, maintain a remain_gas variable
        # start to drive from point a, if remain_gas turns into negative at point b, skip all the candidates between a abd b, but restart from the next starting point b+1.
        # immediate check
        if sum(gas) < sum(cost):
            return -1
        # after te=he former check, a solution always exist
        res = 0
        total = 0
        for i in range(res, len(gas)):
            total += gas[i]-cost[i]
            if total < 0:
                total = 0
                res = i+1
        return res