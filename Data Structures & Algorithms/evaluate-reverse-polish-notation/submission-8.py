class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        answer=[]
        for i in tokens:
            if i not in "+-*/":
                answer.append(int(i))
            else:
                if i=="+":
                    a=answer.pop()
                    b=answer.pop()
                    answer.append(a+b)
                elif i=="*":
                    a=answer.pop()
                    b=answer.pop()
                    answer.append(a*b)
                elif i=="-":
                    a=answer.pop()
                    b=answer.pop()
                    answer.append(b-a)
                elif i=="/":
                    a=answer.pop()
                    b=answer.pop()
                    answer.append(int(b/a))
        return answer[-1]
