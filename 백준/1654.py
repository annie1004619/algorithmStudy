k,n = map(int, input().split())
lines = []
for _ in range(k):
    lines.append(int(input()))

start = 1
end = max(lines)
result = 0

while start <= end:
    count = 0
    mid = (start + end) // 2
    
    for line in lines:
        count += line // mid

    if count < n:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
