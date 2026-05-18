import heapq

def dijkstra(start, graph, n):
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[start] = 0

    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        cost, now = heapq.heappop(heap)

        if dist[now] < cost:
            continue

        for next_node, next_cost in graph[now]:
            new_cost = cost + next_cost

            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))

    return dist


def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]

    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))

    dist_s = dijkstra(s, graph, n)
    dist_a = dijkstra(a, graph, n)
    dist_b = dijkstra(b, graph, n)

    answer = float('inf')

    for i in range(1, n + 1):
        answer = min(
            answer,
            dist_s[i] + dist_a[i] + dist_b[i]
        )

    return answer