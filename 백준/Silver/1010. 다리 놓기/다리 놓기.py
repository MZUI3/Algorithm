'''
재원이는 한 도시의 시장이 되었다.
이 도시에는 도시를 동쪽과 서쪽으로 나누는 큰 일직선 모양의 강이 흐르고 있다.
하지만 재원이는 다리가 없어서 시민들이 강을 건너는데 큰 불편을 겪고 있음을 알고 다리를 짓기로 결심하였다.
강 주변에서 다리를 짓기에 적합한 곳을 사이트라고 한다.
재원이는 강 주변을 면밀히 조사해 본 결과 강의 서쪽에는 N개의 사이트가 있고 동쪽에는 M개의 사이트가 있다는 것을 알았다. (N ≤ M)

재원이는 서쪽의 사이트와 동쪽의 사이트를 다리로 연결하려고 한다.
(이때 한 사이트에는 최대 한 개의 다리만 연결될 수 있다.)
재원이는 다리를 최대한 많이 지으려고 하기 때문에 서쪽의 사이트 개수만큼 (N개) 다리를 지으려고 한다.
다리끼리는 서로 겹쳐질 수 없다고 할 때 다리를 지을 수 있는 경우의 수를 구하는 프로그램을 작성하라.
'''

""" 
얼핏보면 combination 문제로 보이지만, 다리를 겹치게 지으면 안되기 때문에 오히려 다리를 짓지 않는 곳을 정하는 문제이다
두 구조중 게이트 개수가 작은 곳을 정한 뒤에 그곳에 다리를 짓지 않는 문제로 전환하여 풀이한다
예제 입력 1 
3
2 2
1 5
13 29
예제 출력 1 
1
5
67863915
"""

import sys
input = sys.stdin.readline

repreat_t = int(input())

def combination(n, r):
    r = min(r, n - r)
    result = 1
    for i in range(r):
        result = result * (n - i) / (i + 1)
    return int(result)

for _ in range(repreat_t):
    N, M = map(int, input().split())
    
    key = N - M
    
    if key < 0:
        print(combination(M, abs(key)))
    elif key > 0:
        print(combination(N, key))
    else:
        print(1)