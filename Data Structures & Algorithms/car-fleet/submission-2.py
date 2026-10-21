class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 2-axis drawing for position-time is helpful
        # for two cars, if the one at left reaches destination faster or equal to the one at the right side, then they will be a fleet; te last action is delete the one in the feet with the larger speed
        # iterate from right to left, so that we can know for each current car, which car ahead is possible to have collison with it
        # sort based on the position + iteration: O(nlogn) + O(n); SC, a stack: O(n)
        # return the length of the stack->the number of fleets

        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(pair)[::-1]: # reverse sorted order
            stack.append((target - p) / s)
            if len(stack) >=2 and stack[-1]<= stack[-2]:
                stack.pop()
        return len(stack)

