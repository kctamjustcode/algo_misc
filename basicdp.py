## basic dp practise from leetcode

def minCostClimbingStairs(cost) -> int:
    if len(cost) <= 1:
        return 0
    elif len(cost) == 2:
        return min(cost)
    else:
        return min(cost[-1]+minCostClimbingStairs(cost[:-1]), cost[-2]+minCostClimbingStairs(cost[:-2]))
    
print(minCostClimbingStairs([1,1,100,1,60,50,1]))
print(minCostClimbingStairs([10, 15, 20]))


def uniquePathsWO(obstacleGrid) -> int:
    n = len(obstacleGrid[0])
    m = len(obstacleGrid)
    dp = [[0 for i in range(n)] for j in range(m)]
    dp[0][0] = 1 - obstacleGrid[0][0]

    for j in range(1,n):
        if obstacleGrid[0][j] == 0:
            dp[0][j] = dp[0][j-1]

    for i in range(1,m):
        if obstacleGrid[i][0] == 0:
            dp[i][0] = dp[i-1][0]

    for i in range(1,m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 0:
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
    print(dp)
    return dp[-1][-1]

OG = [[0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0],[1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,0],[1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0],[0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],[0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],[0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1],[0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],[1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0],[0,0,0,1,0,0,0,0,1,1,1,0,0,1,0,1,1,0],[0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1],[0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0],[1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0],[1,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1],[1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0]]

def uniquePathsWithObstacles(obstacleGrid) -> int:
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        dp=[[0 for i in range(n)] for j in range(m)]
        dp[0][0]=1-obstacleGrid[0][0]
        for i in range(m):
            for j in range(n):
                if i+1<m and obstacleGrid[i+1][j]==0: dp[i+1][j]+=dp[i][j]
                if j+1<n and obstacleGrid[i][j+1]==0: dp[i][j+1]+=dp[i][j]
        print(dp)
        return dp[-1][-1]

print(uniquePathsWO(OG))
print(uniquePathsWithObstacles(OG))