def solution(n, vertex):
    INF = float('inf')

    dist = [INF] * (n + 1)
    dist[1] = 0

    # Bellman-Ford
    for _ in range(n - 1):
        updated = False

        for a, b in vertex:
            # a -> b
            if dist[a] != INF and dist[b] > dist[a] + 1:
                dist[b] = dist[a] + 1
                updated = True

            # b -> a (양방향)
            if dist[b] != INF and dist[a] > dist[b] + 1:
                dist[a] = dist[b] + 1
                updated = True

        if not updated:
            break

    max_dist = max(dist[1:])
    return dist.count(max_dist)