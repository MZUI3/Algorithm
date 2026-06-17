def solution(land, height):
    N = len(land)
    parent = list(range(N * N))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[ra] = rb
        return True

    max_w = 10000
    buckets = [[] for _ in range(max_w + 1)]

    for i in range(N):
        for j in range(N):
            idx = i * N + j
            if j + 1 < N:
                diff = abs(land[i][j] - land[i][j + 1])
                w = diff if diff > height else 0
                buckets[w].append((idx, idx + 1))
            if i + 1 < N:
                diff = abs(land[i][j] - land[i + 1][j])
                w = diff if diff > height else 0
                buckets[w].append((idx, idx + N))

    total_cost = 0
    edges_used = 0
    target = N * N - 1
    for w in range(max_w + 1):
        if edges_used == target:
            break
        for a, b in buckets[w]:
            if edges_used == target:
                break
            if union(a, b):
                total_cost += w
                edges_used += 1
    return total_cost
