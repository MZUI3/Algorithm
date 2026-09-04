TC = int(input())
for tc in range(1, TC+1):
    n = int(input())
    a = list(map(int, input().split()))
    
    result = sum(1 for i in range(n) if a[i] != i + 1)
    print(f"#{tc} {result:.6f}")