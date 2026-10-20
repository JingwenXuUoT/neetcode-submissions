class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
       # use a stack to record the asteroid that won't collapse in current iteration
       # collapse only appends when the current newly iterating node is negative and the top node in the stack is positive
        # O(n), O(n)
        stack = []
        for a in asteroids:
            while stack and a<0 and stack[-1] >0:
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0 # break the while condition
                else:
                    a = 0
                    stack.pop()
            if a:
                stack.append(a)
        return stack