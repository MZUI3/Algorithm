import sys
input = sys.stdin.readline

W = int(input())

if W >5:
    dp = [-1]*(W + 1)
    dp[3] = 1
    dp[5] = 1
    for i in range(3, W+1):
        if (dp[i -3] != -1):
            dp[i] = dp[i - 3] + 1
        if (dp[i -5] != -1):
            if dp[i] != -1:
                dp[i] = min(dp[i-5]+1, dp[i])
            else:
                dp[i] = dp[i - 5] + 1
    print(dp[W])
else:
    if W == 3 or W == 5:
        print(1)
    else:
        print(-1)