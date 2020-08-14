class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            # print("token is %s, stack is %s" %(token, stack))
            if token.isdigit():
                stack.append(int(token))
            # handle negative numbers
            elif len(token) > 1 and token[0] == '-':
                num = token[1:len(token)]
                stack.append(int(num)*-1)
            else:
                second, first = stack.pop(), stack.pop()
                res = self.evaluate(first, second, token)
                stack.append(res)
            # print("new stack is %s" %stack)
        return stack[0]
    
    
    def evaluate(self, first: int, second: int, op: str) -> int:
        if op == '+':
            return first+second
        elif op == '-':
            return first-second
        elif op == '*':
            return first*second
        else:           
            return int(first/second)
        
        
        
