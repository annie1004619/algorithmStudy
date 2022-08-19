from collections import deque

def solution(maps):
    start=(0,0)

    n = len(maps)
    m = len(maps[0])
    visited = [[0]*m for _ in range(n)]

    dxs=[-1,1,0,0]
    dys=[0,0,-1,1]

    queue = deque([start])
    visited[start[0]][start[1]] = 1

    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs,dys):
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0<= ny < m and maps[nx][ny] == 1: #칸을 넘으면 안되고 
                if not visited[nx][ny] : #방문을 안했을 때 큐에 넣는다. 넣고 방문처리 
                    queue.append([nx,ny])
                    visited[nx][ny] = visited[x][y] + 1 # 거리 계산 

    return visited[-1][-1] if visited[-1][-1] != 0 else -1
    





map = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]

print(solution(map))