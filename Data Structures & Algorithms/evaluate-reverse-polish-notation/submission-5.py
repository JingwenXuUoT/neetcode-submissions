class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "+-*/":
            # if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                # isdigit() and isnumberic() only return True for digits from 0 to 9, should explicitly check negative numbers
                # or if token not in "+-*/"
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                cur_res = a
                if token == "+":
                    cur_res = a + b
                elif token == "-":
                    cur_res = b - a
                elif token == "*":
                    cur_res = a * b
                else:
                    # cur_res = b // a # this shouls always truncated towards zero
                    cur_res = int(b/a) # int() on a float always truncates towards zero regarless of the sign
                stack.append(cur_res)
        return stack[0]