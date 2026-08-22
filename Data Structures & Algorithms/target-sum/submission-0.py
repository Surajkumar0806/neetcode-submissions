class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total:
            return 0 
        if (target + total) % 2 != 0:
            return 0
        
        postive = (target + total) // 2

        dp = [0] * (postive + 1)
        dp[0] = 1
        for num in nums:
            for x in range(postive, num - 1, -1):
                dp[x] += dp[x-num]
        return dp[postive]

