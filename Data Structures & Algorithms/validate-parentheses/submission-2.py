class Solution:
    def isValid(self, s: str) -> bool:
        parenthese_map = {'(': ')', '{': '}', '[': ']'}

        stack = [] # for opening brackets, for order and parathese type

        for string in s:
            if string in parenthese_map:
                stack.append(string)
            elif not stack or parenthese_map[stack[-1]] != string:
                return False
            else:
                stack.pop()
        
        return True if not stack else False
        # the stack should be empty after entire iteration, otherwise the stack is invalid because closing and opening brackets are not balanced

        