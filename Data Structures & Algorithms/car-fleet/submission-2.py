class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        stack2=[]
        stack3=[]
        fleet=1
        for i in range(len(position)-1,-1,-1):
            stack.append((position[i],speed[i]))
        ss=sorted(stack, key=lambda x:x[0], reverse=True)
        for i in range(len(ss)):
            time=(target-ss[i][0])/ss[i][1]
            stack2.append(time)
        print(stack2)
        for i in stack2:
            if not stack3:
                stack3.append(i)
            else:
                if stack3[-1]<i:
                    fleet+=1
                stack3.append(max(i, stack3[-1]))
        return fleet
