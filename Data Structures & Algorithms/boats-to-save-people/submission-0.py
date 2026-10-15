class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # greedy idea: sort, then pair the heaviest with the lightest
        # two pointer
        # O(nlogn)
        people.sort()
        res = 0
        l, r = 0, len(people)-1
        while l<=r:
            # terminal condition: one people left
            remain = limit - people[r]
            r -= 1
            res += 1
            if l<= r and remain >= people[l]:
                l += 1
        return res

        