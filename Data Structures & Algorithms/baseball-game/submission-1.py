class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for token in operations:
            if token == "C":
                stack.pop()
            elif token == "D":
                a=stack[-1]
                stack.append(a*2)
            elif token=="+":
                a=stack[-1]
                b=stack[-2]
                stack.append(a+b)
            else:
                stack.append(int(token))
        return sum(stack)