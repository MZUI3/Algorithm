N = int(input())
P = list(map(int, input().split()))

P.sort()

total = 0
current = 0

for p in P:
    current += p
    total += current

print(total)