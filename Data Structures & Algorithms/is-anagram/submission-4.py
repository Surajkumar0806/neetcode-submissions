class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen={}
        seen2={}
        if len(s)== len(t):
            for i in s:
                if i not in seen:
                    seen[i]=1
                elif i in seen:
                    seen[i] +=1
            for j in t:
                if j not in seen2:
                    seen2[j]=1
                elif j in seen2:
                    seen2[j] +=1
            return seen==seen2
        else:
            return False
            