class Solution:
    def climbStairs(self, n: int) -> int:
        visit = {}
        def ways(n):
            if n == 0:
                return 1
            if n == 1:
                return 1
            if n in visit:
                return visit[n]

            visit[n] = ways(n-1) + ways(n-2)
            
            return visit[n]
        return ways(n)