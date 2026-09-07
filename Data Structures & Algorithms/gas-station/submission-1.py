class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # for each candidate starting point, maintain a remain_gas variable
        # start to drive from point a, if remain_gas turns into negative at point b, skip all the candidates between a abd b, but restart from the next starting point b+1.
        # immediate check
        if sum(gas) < sum(cost):
            return -1
        # after te=he former check, a solution always exist
        startIndex_res = 0
        total_gas = 0
        for i in range(len(gas)):
            total_gas += gas[i]-cost[i]
            if total_gas < 0:
                total_gas = 0
                startIndex_res = i+1
        return startIndex_res