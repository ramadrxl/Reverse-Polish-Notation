class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operators = {"+": lambda x, y: x+y,
                     "-": lambda x, y: x-y,
                     "/": lambda x, y: int(float(x)/y),
                     "*": lambda x, y: x*y
                    }
        for t in tokens:
            if t not in operators.keys():
                stack.append(int(t))           # -203,5
            else:
                r, l = stack.pop(), stack.pop() # -198
                stack.append(operators[t](l,r))
        return stack[0]
        """
        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(l+r)
                elif t == "-":
                    stack.append(l-r)
                elif t == "*":
                    stack.append(l*r)
                else:
                    stack.append(int(float(l)/r))
        return stack.pop() 
        """
