class Solution:
    def checkValidString(self, s: str) -> bool:
        # use two stack, one to track the indices of left par, the other for star indices
        # if current ch is a right par, if left par stack is not empty, pop from it, otherwise, pop from the star stack
        # after iteration, if one or two stacks if not empty, try to match star to left pars.:
        # iteratively pop, pop one from left and one from star stack each step, return False if left indices is larger than the star indices

        # left_stack = []
        # star_stack = []

        # for idx, ch in enumerate(s):
        #     if ch == '(':
        #         left_stack.append(idx)
        #     elif ch == '*':
        #         star_stack.append(idx)
        #     else:
        #         if left_stack:
        #             left_stack.pop()
        #         elif star_stack:
        #             star_stack.pop()
        #         else:
        #             return False
    
        # while left_stack and star_stack:
        #     left_idx = left_stack.pop()
        #     star_idx = star_stack.pop()
        #     if left_idx > star_idx:
        #         return False

        # return not left_stack
        # O(n), O(n)

        # method 2: Greedy
        # tracking a range of possible unmatched '('
        # at any point, only need to know the min and max number
        # if max becomes negative, return False
        # at the end, if min is zero, return True
        # TC: O(n), SC: O(1)
        leftMin = 0
        leftMax = 0
        for c in s:
            if c == '(':
                leftMin, leftMax = leftMin+1, leftMax+1
            elif c == ')':
                leftMin, leftMax = leftMin-1, leftMax-1
            else:
                leftMin, leftMax = leftMin-1, leftMax+1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0