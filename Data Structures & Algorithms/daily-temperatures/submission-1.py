class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        eptstack=[]
        answers=[]       
        for i in range(len(temperatures)-1,-1,-1):
            while eptstack and temperatures[i]>=eptstack[-1][0]:
                eptstack.pop()
            if eptstack:
                answers.append(eptstack[-1][1]-i)
            else:
                answers.append(0)
            eptstack.append((temperatures[i],i))
        answers.reverse()
        return answers