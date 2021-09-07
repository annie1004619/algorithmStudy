n,c = map(int, input().split())
home = []
for _ in range(n):
    home.append(int(input()))
home.sort()

def counter(distance):
    start = home[0]
    count = 1
    for i in range(1,n):
        if start + distance <= home[i]:
            count += 1
            start = home[i]
    return count

start,end = 1, home[-1] - home[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    if (counter(mid) < c):
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)

