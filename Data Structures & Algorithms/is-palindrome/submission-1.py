class Solution:
    def isPalindrome(self, s: str) -> bool:
        sr=""
        for char in s:
            if char.isalnum():
                sr +=char.lower()
        l=0
        r=len(sr)-1
        while l<r:
            if sr[l]!=sr[r]:
                return False
            l +=1
            r -=1
        return True