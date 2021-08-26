from collections import deque
# deque가 queue보다 속도가 훨씬 빠르다고 합니다!


m, n, h = map(int, input().split())
boxes = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

day = 0
ripe_tomato = deque()

dxs = [1, -1, 0, 0, 0, 0]
dys = [0, 0, 1, -1, 0, 0]
dzs = [0, 0, 0, 0, 1, -1]

for z in range(h):
    for x in range(n):
        for y in range(m):
            if boxes[z][x][y] == 1:
                ripe_tomato.append((x, y, z))


def bfs():
    while ripe_tomato:
        x, y, z = ripe_tomato.popleft()
        for dx, dy, dz in zip(dxs, dys, dzs):
            nx, ny, nz = x + dx, y + dy, z + dz
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if boxes[nz][nx][ny] == 0:
                    boxes[nz][nx][ny] = boxes[z][x][y] + 1
                    ripe_tomato.append((nx, ny, nz))


bfs()

for box in boxes:
    for row in box:
        for tomato in row:
            if tomato == 0:
                print(-1)
                exit(0)
            day = max(day, max(row))

print(day - 1)
