def climbStairs(n):
    # dp = [-1]*(n+1)
    # dp[0], dp[1] = 1,1
    # for i in range(2,n+1):
    #     dp[i] = dp[i-1] + dp[i-2]
    
    # return dp[n]
    prev, prev2 = 1,1

    for i in range(2,n+1):
        curr = prev+prev2
        prev2 = prev
        prev = curr
    return prev