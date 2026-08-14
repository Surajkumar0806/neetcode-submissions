class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev1 = 0
        prev2 = 0
        for i in range(n):
            current = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = current
        return prev1