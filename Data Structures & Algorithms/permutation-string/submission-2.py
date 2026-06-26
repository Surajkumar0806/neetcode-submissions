class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqs1={}
        freqs2={}
        l=0
        r=len(s1)
        if len(s2)>=len(s1):
            for i in range(len(s1)):
                freqs1[s1[i]]=1+freqs1.get(s1[i], 0)
            for i in range(l,r):
                freqs2[s2[i]]=1+freqs2.get(s2[i], 0)
            if freqs1==freqs2:
                    return True
            while r<len(s2):
                freqs2[s2[l]]=freqs2.get(s2[l])-1
                freqs2[s2[r]]=1+freqs2.get(s2[r], 0)
                if freqs2[s2[l]]==0:
                    del freqs2[s2[l]]
                if freqs1==freqs2:
                    return True
                l+=1
                r+=1
            return False
        else:
            return False
