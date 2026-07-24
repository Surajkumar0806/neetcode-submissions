class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left=0
        right=0
        checked=None
        while right < len(t) and left < len(s):
            checked=False
            if s[left]==t[right]:
                left+=1
            right+=1
        return left==len(s)
            
