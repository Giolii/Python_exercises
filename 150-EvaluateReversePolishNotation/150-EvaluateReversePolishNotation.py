# Last updated: 7/10/2025, 4:46:33 PM
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
        '+': lambda a,b : a + b,
        '-': lambda a,b : a - b,
        '*': lambda a,b : a * b,
        '/': lambda a,b : int(a / b),
        }
        
        stack = []
        for tok in tokens:
            if tok not in operations:
                stack.append(int(tok))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                result = operations[tok](num1,num2) 
                stack.append(result)
        return stack[-1]
        