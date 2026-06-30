class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
                            "+": lambda a, b: b + a,
                            "-": lambda a, b: b - a,
                            "*": lambda a, b: b * a,
                            "/": lambda a, b: int(b / a)
                     }
        stack=[]
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(operations[token](a, b)) 
        return stack[-1]