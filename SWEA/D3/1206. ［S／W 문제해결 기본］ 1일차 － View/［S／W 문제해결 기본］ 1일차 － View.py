for tc in range(10):
    N = int(input())
    height = list(map(int, input().split()))
    total = 0
    for i in range(2, N-2):
        side_height = max(height[i-1], height[i-2], height[i+1], height[i+2])
        if side_height < height[i]:
            total += (height[i] - side_height)

    print(f"#{tc+1} {total}")