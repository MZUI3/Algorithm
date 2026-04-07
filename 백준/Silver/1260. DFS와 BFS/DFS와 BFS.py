from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

visited = [False] * (N+1)

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

dfs(V)
print()

visited = [False] * (N+1)

def bfs(v):
    queue = deque([v])
    visited[v] = True
    
    while queue:
        x = queue.popleft()
        print(x, end=' ')
        
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

bfs(V)