class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        # standing at a future index, compute all the results of the pervious indexes that's lower than this future value
        # use a stack to maintain indices in a monotonically decreasing order, poping indices where the values are smaller than the current element
        # for a already decreasing order subarray, no pop;
        # when the stack is no longer decreasing, we pop the elements from the stack until the top is no less than the current element
        stack = []
        for i, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                cur_idx = stack.pop()
                res[cur_idx] = i - cur_idx
            stack.append(i)
            # the stack only ever needs one index-value pair per entry, so a tuple is simpler
        
        return res