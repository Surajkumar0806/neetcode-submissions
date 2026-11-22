class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = {}
        freq2 = {}
        left = 0
        right = len(s1)
        if len(s2) < len(s1):
            return False
        for i in range(len(s1)):
            freq1[s1[i]] = 1 + freq1.get(s1[i], 0)
        for i in range(left, right):
            freq2[s2[i]] = 1 + freq2.get(s2[i], 0)
        if freq1 == freq2:
            return True
        while right < len(s2):
            freq2[s2[left]] = freq2.get(s2[left]) - 1
            freq2[s2[right]] = 1 + freq2.get(s2[right], 0)
            if freq2[s2[left]] == 0:
                del freq2[s2[left]]
            if freq1 == freq2:
                return True
            left+=1
            right+=1
        return False
    