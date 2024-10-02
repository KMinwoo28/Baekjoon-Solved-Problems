import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

V = int(input())
E = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A].append((C, A, B))
    graph[B].append((C, B, A))

def prim(start_node):
    visited = [False]*(V+1)
    visited[start_node] = True
    MST = [] # MST path
    candidate = graph[start_node] # T와 T에 없는 노드를 잇는 간선이 들어있는 최소힙
    total_weight = 0
    heapq.heapify(candidate)
    
    while candidate:
        w, x, y = heapq.heappop(candidate) 
        
        if visited[y] == False:
            visited[y] = True
            MST.append((x, y))
            total_weight += w
            
            for edge in graph[y]:
                if visited[edge[2]] == False:
                    heapq.heappush(candidate, edge)
                    
    return MST, total_weight
                
path_MST, total_weight = prim(1)
print(total_weight)