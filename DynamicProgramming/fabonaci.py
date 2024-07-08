# Memoization:
def f(n, dp):
    if (n<=1):
        return n
    
    if (dp[n]!=-1):
        return dp[n]
    dp[n] = f(n-1, dp)+ f(n-2, dp)
    return dp[n]

# Tabulation:
def ft(n, dp):
    dp[0]=0
    dp[1]=1
    for i in range(2,n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]

# space-optimized function:
def fo(n):
    prev = 1
    prev2 = 0
    for i in range(2,n+1):
        curri = prev+prev2
        prev2 = prev
        prev = curri
    return prev


def main():
    n = int(input("Enter the val: "))
    dp =[-1]*(n+1)
    # ans = ft(n, dp)
    ans = fo(n)
    print("ans: ", ans)

main()
