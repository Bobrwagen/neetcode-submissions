class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        cur = 0
        for i in range(n):
            cur += grid[0][i]
            dp[0][i] = cur
        cur = 0
        for j in range(m):
            cur += grid[j][0]
            dp[j][0] = cur
        for i in range(1, n):
            for j in range(1, m):
                dp[j][i] = grid[j][i] + min(dp[j][i-1], dp[j-1][i])
        return dp[-1][-1]