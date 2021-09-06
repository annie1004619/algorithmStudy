from collections import deque

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
result_matrix = [[0]*n for _ in range(n)]
list = [[] for _ in range(n)]
route = deque()

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            list[i].append((i,j))

def bfs(s):
    if not list[s]: return
    for x,y in list[s]:
        route.append((x,y))
    while route:
        x,y = route.popleft()
        if result_matrix[s][y] == 0:
            result_matrix[s][y] = 1
            if list[y]:
                for i,j in list[y]:
                    route.append((i,j))    

for i in range(n):
    bfs(i)

for row in result_matrix:
    print(' '.join(map(str, row)))