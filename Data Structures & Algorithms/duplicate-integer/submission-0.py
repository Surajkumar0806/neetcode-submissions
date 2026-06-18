class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
            seen=set()
            for i in nums:
                if i in seen:
                    return True 
                elif i not in seen:
                    seen.add(i)
            return False  