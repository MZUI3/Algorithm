import sys
input = sys.stdin.readline

N, D = map(int, input().split())

shortcuts = []
for _ in range(N):
    s, e, c = map(int, input().split())
    if e <= D and c < (e - s):
        shortcuts.append((s, e, c))

shortcuts.sort()

dp = [float('inf')] * (D + 1)
dp[0] = 0

idx = 0

for i in range(D + 1):
    if i > 0:
        dp[i] = min(dp[i], dp[i-1] + 1)

    while idx < len(shortcuts) and shortcuts[idx][0] == i:
        s, e, c = shortcuts[idx]
        dp[e] = min(dp[e], dp[i] + c)
        idx += 1

print(dp[D])