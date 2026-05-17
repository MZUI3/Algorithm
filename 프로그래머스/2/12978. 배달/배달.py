import heapq

def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[1] = 0
    
    heap = []
    heapq.heappush(heap, (0, 1))
    
    while heap:
        current_dist, now = heapq.heappop(heap)
        
        if current_dist > dist[now]:
            continue
        
        for next_node, cost in graph[now]:
            new_cost = current_dist + cost
            
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))
    
    answer = 0
    
    for d in dist:
        if d <= K:
            answer += 1
    
    return answer